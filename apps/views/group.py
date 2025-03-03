from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.models import Group, Attendance
from apps.serializer import GroupModelSerializer


@extend_schema(
    tags=['groups'],
)
class GroupCreateApiView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


@extend_schema(
    tags=['groups'],
)
class GroupListApiView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


@extend_schema(
    tags=['groups'],
)
class GroupDetailApiView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['groups'],
)
class GroupUpdateApiView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['groups'],
)
class GroupDeleteApiView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


from datetime import datetime, timedelta
from django.db.models import Exists, OuterRef


def get_lesson_statuses(group_id):
    """ Guruhda dars bo‘lishi kerak bo‘lgan kunlarning o‘tilgan va o‘tilmagan holatini chiqarish """
    group = Group.objects.get(id=group_id)

    start_date = group.date.date()  # Guruh ochilgan sana
    end_date = datetime.today().date()  # Bugungi sana

    # Guruhda dars bo‘ladigan hafta kunlari
    lesson_days = {day.name.lower() for day in group.days.all()}

    missed_lessons = []
    attended_lessons = []
    current_date = start_date

    while current_date <= end_date:
        weekday = current_date.strftime('%A').lower()  # Sana hafta kuniga o‘giriladi

        if weekday in lesson_days:
            # Ushbu sanada dars bor-yo‘qligini tekshiramiz
            if Attendance.objects.filter(group=group, date=current_date).exists():
                attended_lessons.append(current_date.strftime("%Y-%m-%d"))
            else:
                missed_lessons.append(current_date.strftime("%Y-%m-%d"))

        current_date += timedelta(days=1)  # Kunni oldinga siljitish

    return {"attended": attended_lessons, "missed": missed_lessons}


from rest_framework.views import APIView
from rest_framework.response import Response


@extend_schema(
    tags=['groups'],
)
class LessonStatusesView(APIView):
    def get(self, request, pk):
        lesson_statuses = get_lesson_statuses(pk)
        return Response({
            "group_id": pk,
            "attended_lessons": lesson_statuses["attended"],
            "missed_lessons": lesson_statuses["missed"]
        })

import datetime

from django.db.models import Q
from django.utils.dateparse import parse_date
from drf_spectacular.utils import extend_schema
from requests import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Attendance
from apps.serializer import AttendanceModelSerializer, AttendanceSearchFilterSerializer


@extend_schema(
    tags=['attendance'],
)
class AttendanceCreateAPIView(CreateAPIView):
    serializer_class = AttendanceModelSerializer
    queryset = Attendance.objects.all()


@extend_schema(
    tags=['attendance'],
)
class AttendanceListAPIView(ListAPIView):
    queryset = Attendance.objects.filter(date=datetime.date.today()).all()
    serializer_class = AttendanceModelSerializer


@extend_schema(
    tags=['attendance'],
)
class AttendanceDetailAPIView(RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


@extend_schema(
    tags=['attendance'],
)
class AttendanceUpdateAPIView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


@extend_schema(
    request=AttendanceSearchFilterSerializer,
    tags=['attendance'],
    responses=AttendanceModelSerializer, )
class AttendanceFilterSearchAPIView(APIView):
    def post(self, request):
        date = request.data.get("date")  # Sana olish
        search_query = request.data.get("search", "").strip()  # Qidiruv so‘rovi
        branch = request.data.get("branch")  # Branch ID olish

        if not date or not parse_date(date):
            return Response({"error": "date noto‘g‘ri yoki mavjud emas."}, status=status.HTTP_400_BAD_REQUEST)

        date = parse_date(date)

        queryset = Attendance.objects.filter(date=date)

        if branch:
            queryset = queryset.filter(employee__smina__branches=branch)

        if search_query:
            queryset = queryset.filter(Q(employee__full_name__icontains=search_query))

        if not queryset.exists():
            return Response({"message": "Berilgan sana bo‘yicha hech qanday natija topilmadi."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = AttendanceModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# @extend_schema(
#     tags=['attendance'],
# )
# class AttendanceSearchApiView(APIView):
#     queryset = count(Attendance.objects.all(date=datetime.date.today()).all())
#
#

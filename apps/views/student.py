from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView

from apps.models import Student
from apps.serializer import StudentModelSerializer


@extend_schema(
    tags=['student'],
)
class StudentCreateApiView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


@extend_schema(
    tags=['student'],
)
class StudentListApiView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


@extend_schema(
    tags=['student'],
)
class StudentDetailApiView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['student'],
)
class StudentUpdateApiView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['student'],
)
class StudentTeacherApiView(APIView):
    def get(self, request):
        print(request.user)


@extend_schema(
    tags=['student'],
)
class StudentDeleteApiView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

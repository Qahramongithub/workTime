from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import Employee
from apps.serializer import EmployeeSerializer


@extend_schema(
    tags=['employee'],
    request=EmployeeSerializer,
    responses=EmployeeSerializer,
)
class EmployeeCreateApiView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = AllowAny,




@extend_schema(
    tags=['employee'],
)
class EmployeeListApiView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@extend_schema(
    tags=['employee'],
)
class EmployeeRetrieveApiView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['employee'],
)
class EmployeeUpdateApiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['employee'],
)
class OneEmployeeListApiView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        query = super().get_queryset()
        pk = self.kwargs.get('pk')
        query = query.filter(pk=pk)
        return query


@extend_schema(
    tags=['employee'],
)
class EmployeeDeleteApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['employee'],
)
class TeacherEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        query = super().get_queryset()
        pk = self.kwargs.get('pk')
        query = query.filter(position=pk)
        return query

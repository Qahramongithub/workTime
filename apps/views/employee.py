from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from apps.models import Employee
from apps.serializer import EmployeeModelSerializer


@extend_schema(
    tags=['employee'],
)
class EmployeeCreateApiView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer


@extend_schema(
    tags=['employee'],
)
class EmployeeListApiView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer


@extend_schema(
    tags=['employee'],
)
class EmployeeRetrieveApiView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


@extend_schema(
    tags=['employee'],
)
class EmployeeUpdateApiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


@extend_schema(
    tags=['employee'],
)
class OneEmployeeListApiView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get_queryset(self):
        query = super().get_queryset()
        pk = self.kwargs.get('pk')
        query = query.filter(pk=pk)
        return query

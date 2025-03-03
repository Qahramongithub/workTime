from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    RetrieveAPIView, DestroyAPIView

from apps.models import Branch, Day
from apps.serializer import BranchModelSerializer, DayModelSerializer


@extend_schema(
    tags=['branch']
)
class BranchCreateApiView(CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer


@extend_schema(
    tags=['branch']
)
class BranchListApiView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer


@extend_schema(
    tags=['branch']
)
class BranchUpdateApiView(UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['branch']
)
class BranchDetailApiView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['branch']
)
class BranchDeleteApiView(DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['day']
)
class DayListApiView(ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DayModelSerializer


@extend_schema(
    tags=['day']
)
class DayCreateApiView(CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DayModelSerializer


@extend_schema(
    tags=['day']
)
class DayUpdateApiView(UpdateAPIView):
    queryset = Day.objects.all()
    serializer_class = DayModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['day']
)
class DayDetailApiView(RetrieveAPIView):
    queryset = Day.objects.all()
    serializer_class = DayModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['day']
)
class DayDeleteApiView(DestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DayModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

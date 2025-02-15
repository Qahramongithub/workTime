from django.utils.translation.trans_real import activate
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from apps.models import Branch, Shift
from apps.serializer import BranchModelSerializer, ShiftModelSerializer


@extend_schema(
    tags=['branch'],
)
class BranchCreateApiView(CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer


@extend_schema(
    tags=['branch'],
)
class BranchListApiView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer

    def list(self, request, *args, **kwargs):
        lang = request.headers.get('Accept-Language', 'uz')  # Standart til `uz`
        activate(lang)  # Tarjima tilini faollashtiramiz
        response = super().list(request, *args, **kwargs)
        return Response(response.data)


@extend_schema(
    tags=['branch'],
)
class BranchDetailApiView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    lookup_field = 'id'


@extend_schema(
    tags=['branch'],
)
class BranchUpdateApiView(UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    lookup_field = 'id'


# ================================== shift ========================================================

@extend_schema(
    tags=['shift']
)
class ShiftCreateApiView(CreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftModelSerializer


@extend_schema(
    tags=['shift']
)
class ShiftListApiView(ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftModelSerializer


@extend_schema(
    tags=['shift']
)
class ShiftDetailApiView(RetrieveAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftModelSerializer
    lookup_field = 'id'


@extend_schema(
    tags=['shift']
)
class ShiftUpdateApiView(UpdateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftModelSerializer
    lookup_field = 'id'

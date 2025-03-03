from django.utils.translation.trans_null import activate
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from apps.models import Position
from apps.serializer import PositionModelSerializer


@extend_schema(
    tags=['position']
)
class PositionCreateApiView(CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionModelSerializer


@extend_schema(
    tags=['position']
)
class PositionListApiView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionModelSerializer

    def list(self, request, *args, **kwargs):
        lang = request.headers.get('Accept-Language', 'uz')  # Standart til `uz`
        activate(lang)  # Tarjima tilini faollashtiramiz
        response = super().list(request, *args, **kwargs)
        return Response(response.data)


@extend_schema(
    tags=['position']
)
class PositionDetailApiView(RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['position']
)
class PositionUpdateApiView(UpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['position']
)
class PositionDeleteApiView(DestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

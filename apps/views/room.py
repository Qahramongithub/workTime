from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.models import Room
from apps.serializer import RoomModelSerializer


@extend_schema(
    tags=['room']
)
class RoomCreateApiView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


@extend_schema(
    tags=['room']
)
class RoomListApiView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


@extend_schema(
    tags=['room']
)
class RoomDetailApiView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['room']
)
class RoomUpdateApiView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


@extend_schema(
    tags=['room']
)
class RoomDeleteApiView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

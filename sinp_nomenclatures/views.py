import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Item, Source, Type
from .serializers import (
    ItemSerializer,
    SourceSerializer,
    TypeSerializer,
)

logger = logging.getLogger(__name__)


class ItemViewset(ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()


class TypeViewset(ReadOnlyModelViewSet):
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()


class SourceViewset(ReadOnlyModelViewSet):
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Source.objects.all()


# Create your views here.

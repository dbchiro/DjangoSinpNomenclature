import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Nomenclature, Source, Type
from .serializers import (
    NomenclatureSerializer,
    SourceSerializer,
    TypeSerializer,
)

logger = logging.getLogger(__name__)


class NomenclatureViewset(ReadOnlyModelViewSet):
    serializer_class = NomenclatureSerializer
    permission_classes = [IsAuthenticated]
    queryset = Nomenclature.objects.all()


class TypeViewset(ReadOnlyModelViewSet):
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()


class SourceViewset(ReadOnlyModelViewSet):
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Source.objects.all()


# Create your views here.

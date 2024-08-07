#!/usr/bin/env python3
"""Django SINP Nomenclatures API Views"""


import logging

from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend

# from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Nomenclature, Source, Type
from .serializers import (
    NomenclatureSerializer,
    SourceSerializer,
    TypeSerializer,
    TypeSerializerWithNomenclature,
)

logger = logging.getLogger(__name__)


class NomenclatureViewset(ReadOnlyModelViewSet):
    """Nomenclature item viewset (ReadOnly)"""

    serializer_class = NomenclatureSerializer
    permission_classes = [IsAuthenticated]
    queryset = Nomenclature.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type", "code", "active"]


class TypeViewset(ReadOnlyModelViewSet):
    """Nomenclature type viewset (ReadOnly)"""

    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code", "mnemonic", "source", "status"]

    def get_serializer_class(self):
        with_nomenclatures = self.request.query_params.get(
            "with_nomenclatures", default=False
        )
        return (
            TypeSerializerWithNomenclature
            if with_nomenclatures
            else TypeSerializer
        )

    def get_queryset(self):
        qs = super().get_queryset()
        with_nomenclatures = self.request.query_params.get(
            "with_nomenclatures", default=False
        )
        active = self.request.query_params.get("active", default=None)
        if with_nomenclatures and active:
            if active.lower() in ["true", "1", "t", "y", "yes"]:
                qs = qs.prefetch_related(
                    Prefetch(
                        "nomenclatures",
                        queryset=Nomenclature.objects.filter(active=True),
                    )
                )
            if active.lower() in ["false", "0", "f", "n", "no"]:
                qs = qs.prefetch_related(
                    Prefetch(
                        "nomenclatures",
                        queryset=Nomenclature.objects.filter(active=False),
                    )
                )
        return qs


class SourceViewset(ReadOnlyModelViewSet):
    """Source viewset (ReadOnly)"""

    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Source.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

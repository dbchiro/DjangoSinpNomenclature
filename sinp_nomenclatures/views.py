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
    NomenclatureWithParentsSerializer,
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
    filterset_fields = ["type", "code", "status", "parents"]

    def get_serializer_class(self):
        """Choose simple serializer or serializer serializer with parents"""
        with_parents = self.request.query_params.get(
            "with_parents", default=False
        )
        return (
            NomenclatureWithParentsSerializer
            if with_parents
            else NomenclatureSerializer
        )


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
        nomenclature_status = self.request.query_params.getlist(
            "nomenclature_status", default=None
        )
        if with_nomenclatures and nomenclature_status:
            qs = qs.prefetch_related(
                Prefetch(
                    "nomenclatures",
                    queryset=Nomenclature.objects.filter(
                        status__in=[
                            status.upper() for status in nomenclature_status
                        ]
                    ),
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

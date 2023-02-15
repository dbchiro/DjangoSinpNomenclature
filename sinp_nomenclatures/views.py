#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Django SINP Nomenclatures API Views"""


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
    """Nomenclature item viewset (ReadOnly)"""

    serializer_class = NomenclatureSerializer
    permission_classes = [IsAuthenticated]
    queryset = Nomenclature.objects.all()


class TypeViewset(ReadOnlyModelViewSet):
    """Nomenclature type viewset (ReadOnly)"""

    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()


class SourceViewset(ReadOnlyModelViewSet):
    """Source viewset (ReadOnly)"""

    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Source.objects.all()


# Create your views here.

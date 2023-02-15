#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Django SINP Nomenclatures API serializers"""

from rest_framework.serializers import ModelSerializer

from .models import Nomenclature, Source, Type


class NomenclatureSerializer(ModelSerializer):
    """Nomenclature item serializer"""

    class Meta:
        model = Nomenclature
        fields = ["id", "code", "mnemonic", "label", "type"]


class TypeSerializer(ModelSerializer):
    """Nomenclature type serializer"""

    item_nomenclature = NomenclatureSerializer(many=True)

    class Meta:  # noqa
        model = Type
        fields = ["id", "code", "mnemonic", "label", "item_nomenclature"]


class SourceSerializer(ModelSerializer):
    """Nomenclature source serializer"""

    class Meta:
        model = Source
        fields = ["id", "name", "version"]

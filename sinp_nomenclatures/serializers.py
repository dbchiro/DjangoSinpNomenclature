#!/usr/bin/env python3
"""Django SINP Nomenclatures API serializers"""

from rest_framework.serializers import ModelSerializer

from .models import Nomenclature, Source, Type


class NomenclatureSerializer(ModelSerializer):
    """Nomenclature item serializer"""

    class Meta:
        model = Nomenclature
        fields = ["id", "code", "label", "type", "status", "parents"]


class NomenclatureWithParentsSerializer(ModelSerializer):
    """Nomenclature item serializer"""

    parents = NomenclatureSerializer(many=True)

    class Meta:
        model = Nomenclature
        fields = ["id", "code", "label", "type", "parents", "status"]


class TypeSerializer(ModelSerializer):
    """Nomenclature type serializer"""

    class Meta:  # noqa
        model = Type
        fields = ["id", "code", "mnemonic", "label"]


class TypeSerializerWithNomenclature(ModelSerializer):
    """Nomenclature type serializer"""

    nomenclatures = NomenclatureSerializer(many=True)

    class Meta:  # noqa
        model = Type
        fields = ["id", "code", "mnemonic", "label", "nomenclatures"]


class SourceSerializer(ModelSerializer):
    """Nomenclature source serializer"""

    class Meta:
        model = Source
        fields = ["id", "name", "version"]

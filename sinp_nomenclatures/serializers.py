from rest_framework.serializers import ModelSerializer
from .models import (
    Source,
    Type,
    Nomenclature,
)


class NomenclatureSerializer(ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = ["id", "code", "mnemonic", "label", "type"]


class TypeSerializer(ModelSerializer):
    item_nomenclature = NomenclatureSerializer(many=True)

    class Meta:
        model = Type
        fields = ["id", "code", "mnemonic", "label", "item_nomenclature"]


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = ["id", "name", "version"]

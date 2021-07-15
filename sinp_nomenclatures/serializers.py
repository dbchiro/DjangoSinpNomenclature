from rest_framework.serializers import ModelSerializer
from .models import (
    Source,
    Type,
    Item,
)


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "code", "mnemonic", "label", "type"]


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "code", "mnemonic", "label"]


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = ["id", "name", "version"]

"""Models managers"""

from django.db import models


class SourceManager(models.Manager):
    def get_by_natural_key(self, name, version):
        return self.get(name=name, version=version)


class TypeManager(models.Manager):
    def get_by_natural_key(self, code):
        return self.get(code=code)


class NomenclatureManager(models.Manager):
    def get_by_natural_key(self, nomenclature_type, code):
        return self.get(type=nomenclature_type, code=code)

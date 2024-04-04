"""Models managers"""

from django.db import models


class SourceManager(models.Manager):
    """Source manager"""

    def get_by_natural_key(self, name, version):
        """Get by natural key function"""
        return self.get(name=name, version=version)


class TypeManager(models.Manager):
    """Nomenclature types manager"""

    def get_by_natural_key(self, code):
        """Get by natural key function"""
        return self.get(code=code)


class NomenclatureManager(models.Manager):
    """Nomenclatures manager"""

    def get_by_natural_key(self, nomenclature_type, code):
        """Get by natural key function"""
        return self.get(type__code=nomenclature_type, code=code)

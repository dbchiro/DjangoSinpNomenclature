#!/usr/bin/env python3
"""Django SINP Nomenclatures Models"""


from django.db import models
from django.utils.translation import gettext as _

from sinp_nomenclatures.manager import (
    NomenclatureManager,
    SourceManager,
    TypeManager,
)

# Create your models here.
TYPE_STATUS_CHOICES = (
    ("VALID", _("Valid")),
    ("FREEZE", _("Frozen")),
)

ITEM_STATUS_CHOICES = (
    ("ENABLED", _("Active")),
    ("DISABLED", _("Disabled")),
    ("HIDDEN", _("Hidden")),
)


class BaseModel(
    models.Model
):  # base class should subclass 'django.db.models.Model'
    """Common shared base model with metadata fields"""

    timestamp_create = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp_update = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Source(BaseModel):
    """Source model, giving nomenclature source

    Args:
        BaseModel ([type]): [description]

    Returns:
        [type]: [description]
    """

    objects = SourceManager()
    name = models.CharField(_("Name"), max_length=50)
    version = models.CharField(_("Version"), max_length=50)
    url = models.URLField(_("URL"), max_length=250, blank=True)
    create_date = models.DateField(
        _("Official creation date"), auto_now=False, auto_now_add=False
    )
    update_date = models.DateField(
        _("Official modification date"),
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = _("source")
        verbose_name_plural = _("sources")
        unique_together = ["name", "version"]

    def __str__(self):
        return f"{self.name} ({self.version})"

    def natural_key(self):
        return (self.name, self.version)


class Type(BaseModel):
    """SINP Nomenclature type"""

    objects = TypeManager()
    code = models.CharField(
        _("Code"), unique=True, max_length=50, db_index=True
    )
    mnemonic = models.CharField(_("Mnemonic"), unique=True, max_length=50)
    label = models.CharField(_("Label"), max_length=50)
    status = models.CharField(
        _("Status"),
        max_length=50,
        choices=TYPE_STATUS_CHOICES,
        default=TYPE_STATUS_CHOICES[0][0],
    )
    create_date = models.DateField(
        _("Official creation date"), auto_now=False, auto_now_add=False
    )
    update_date = models.DateField(
        _("Official modification date"),
        auto_now=False,
        auto_now_add=False,
    )
    source = models.ForeignKey(
        "Source",
        verbose_name=_("Source"),
        on_delete=models.CASCADE,
        related_name="type_nomenclature",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Type of nomenclature")
        verbose_name_plural = _("Type of nomenclatures")

    def __str__(self):
        return f"{self.code} - {self.mnemonic}"

    def natural_key(self):
        return (self.code,)


class Nomenclature(BaseModel):
    objects = NomenclatureManager()
    type = models.ForeignKey(
        "Type",
        verbose_name=_("Type"),
        on_delete=models.CASCADE,
        related_name="nomenclatures",
    )
    code = models.CharField(
        max_length=255, db_index=True, verbose_name=_("Code")
    )
    label = models.CharField(max_length=255, verbose_name=_("Label"))
    description = models.TextField(_("Description"), blank=True)
    status = models.CharField(
        _("Usage status"),
        max_length=50,
        choices=ITEM_STATUS_CHOICES,
        default=ITEM_STATUS_CHOICES[0][0],
    )

    parents = models.ManyToManyField(
        "Nomenclature",
        verbose_name=_("Parents nomenclature"),
        related_name="child_nomenclatures",
        blank=True,
    )

    class Meta:
        verbose_name_plural = _("nomenclatures")
        unique_together = ("type", "code")

    def __str__(self):
        return f"{self.label}"

    def natural_key(self):
        return (self.type.code, self.code)

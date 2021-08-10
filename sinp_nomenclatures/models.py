#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.
STATUS_CHOICES = (
    ("VALID", _("Valide")),
    ("FREEZE", _("Gelée")),
)


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'
    """Common shared base model with metadata fields
    """
    timestamp_create = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp_update = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True



class Source(BaseModel):
    """Source model, giving nomenclature source

    Args:
        BaseModel ([type]): [description]

    Returns:
        [type]: [description]
    """
    name = models.CharField(_("Nom"), max_length=50)
    version = models.CharField(_("Version"), max_length=50)
    create_date = models.DateField(
        _("Date de création officielle"), auto_now=False, auto_now_add=False
    )
    update_date = models.DateField(
        _("Date de modification officielle"), auto_now=False, auto_now_add=False
    )

    class Meta:
        verbose_name = _("Source de nomenclatures")
        verbose_name_plural = _("Sources de nomenclatures")
        unique_together = ['name','version']

    def __str__(self):
        return f"{self.name} ({self.version})"

class Type(BaseModel):
    code = models.CharField(_("Code"), unique=True, max_length=50, db_index=True)
    mnemonic = models.CharField(_("Mnémonique"), unique=True, max_length=50)
    label = models.CharField(_("Libellé"), max_length=50)
    status = models.CharField(_("Statut"),max_length=50, choices=STATUS_CHOICES)
    create_date = models.DateField(
        _("Date de création officielle"), auto_now=False, auto_now_add=False
    )
    update_date = models.DateField(
        _("Date de modification officielle"), auto_now=False, auto_now_add=False
    )
    source = models.ForeignKey(
        "Source",
        verbose_name=_("Source"),
        on_delete=models.CASCADE,
        related_name="type_nomenclature",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Type de nomenclature")
        verbose_name_plural = _("Types de nomenclatures")

    def __str__(self):
        return f"{self.code} - {self.mnemonic}"

class Nomenclature(BaseModel):
    type = models.ForeignKey(
        "Type",
        verbose_name=_("Type"),
        on_delete=models.CASCADE,
        related_name="item_nomenclature",
    )
    code = models.CharField(max_length=255, db_index=True, verbose_name=_("Code"))
    mnemonic = models.CharField(_("Mnémonique"), max_length=50)
    label = models.CharField(max_length=255, verbose_name=_("Libellé"))
    description = models.TextField(_("Description"), blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name=_("Est utilisé"))

    class Meta:
        verbose_name_plural = _("nomenclatures")
        unique_together = ("type", "code")

    def __str__(self):
        return f"{self.label}"

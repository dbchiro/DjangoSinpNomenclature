#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Django SINP Nomenclatures Models"""


from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
STATUS_CHOICES = (
    ("VALID", _("Valid")),
    ("FREEZE", _("Frozen")),
)


class BaseModel(
    models.Model
):  # base class should subclass 'django.db.models.Model'
    """Common shared base model with metadata fields"""

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

    name = models.CharField(_("Name"), max_length=50)
    version = models.CharField(_("Version"), max_length=50)
    create_date = models.DateField(
        _("Official creation date"), auto_now=False, auto_now_add=False
    )
    update_date = models.DateField(
        _("Official modification date"),
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = _("Nomenclature source")
        verbose_name_plural = _("Nomenclature sources")
        unique_together = ["name", "version"]

    def __str__(self):
        return f"{self.name} ({self.version})"


class Type(BaseModel):
    code = models.CharField(
        _("Code"), unique=True, max_length=50, db_index=True
    )
    mnemonic = models.CharField(_("Mnemonic"), unique=True, max_length=50)
    label = models.CharField(_("Label"), max_length=50)
    status = models.CharField(
        _("Status"), max_length=50, choices=STATUS_CHOICES
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


class Nomenclature(BaseModel):
    type = models.ForeignKey(
        "Type",
        verbose_name=_("Type"),
        on_delete=models.CASCADE,
        related_name="nomenclatures",
    )
    code = models.CharField(
        max_length=255, db_index=True, verbose_name=_("Code")
    )
    mnemonic = models.CharField(_("Mnemonic"), max_length=50)
    label = models.CharField(max_length=255, verbose_name=_("Label"))
    description = models.TextField(_("Description"), blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name=_("Is used"))
    parent = models.ForeignKey(
        "Nomenclature",
        verbose_name=_("Parent nomenclature"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="child_nomenclature",
    )

    class Meta:
        verbose_name_plural = _("nomenclatures")
        unique_together = ("type", "code")

    def __str__(self):
        return f"{self.label}"

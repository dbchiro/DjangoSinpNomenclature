# Generated by Django 3.2.5 on 2021-07-15 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50, verbose_name="Nom")),
                (
                    "version",
                    models.CharField(max_length=50, verbose_name="Version"),
                ),
                (
                    "create_date",
                    models.DateField(
                        verbose_name="Date de création officielle"
                    ),
                ),
                (
                    "update_date",
                    models.DateField(
                        verbose_name="Date de modification officielle"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Source de nomenclatures",
                "verbose_name_plural": "Sources de nomenclatures",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        unique=True,
                        verbose_name="Code",
                    ),
                ),
                (
                    "mnemonic",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Mnémonique"
                    ),
                ),
                (
                    "label",
                    models.CharField(max_length=50, verbose_name="Libellé"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("VALID", "Valide"), ("FREEZE", "Gelée")],
                        max_length=50,
                        verbose_name="Statut",
                    ),
                ),
                (
                    "create_date",
                    models.DateField(
                        verbose_name="Date de création officielle"
                    ),
                ),
                (
                    "update_date",
                    models.DateField(
                        verbose_name="Date de modification officielle"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="type_nomenclature",
                        to="sinp_nomenclatures.source",
                        verbose_name="Source",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Type de nomenclature",
                "verbose_name_plural": "Types de nomenclatures",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Code"
                    ),
                ),
                (
                    "mnemonic",
                    models.CharField(max_length=50, verbose_name="Mnémonique"),
                ),
                (
                    "label",
                    models.CharField(max_length=255, verbose_name="Libellé"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Description"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True, verbose_name="Est utilisé"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_nomenclature",
                        to="sinp_nomenclatures.type",
                        verbose_name="Type",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "nomenclatures",
                "unique_together": {("type", "code")},
            },
        ),
    ]

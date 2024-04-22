# Generated by Django 4.2.11 on 2024-04-22 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                (
                    "version",
                    models.CharField(max_length=50, verbose_name="Version"),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True, max_length=250, verbose_name="URL"
                    ),
                ),
                (
                    "create_date",
                    models.DateField(verbose_name="Official creation date"),
                ),
                (
                    "update_date",
                    models.DateField(
                        verbose_name="Official modification date"
                    ),
                ),
            ],
            options={
                "verbose_name": "source",
                "verbose_name_plural": "sources",
                "unique_together": {("name", "version")},
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
                        max_length=50, unique=True, verbose_name="Mnemonic"
                    ),
                ),
                (
                    "label",
                    models.CharField(max_length=50, verbose_name="Label"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("VALID", "Valid"), ("FREEZE", "Frozen")],
                        max_length=50,
                        verbose_name="Status",
                    ),
                ),
                (
                    "create_date",
                    models.DateField(verbose_name="Official creation date"),
                ),
                (
                    "update_date",
                    models.DateField(
                        verbose_name="Official modification date"
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
            ],
            options={
                "verbose_name": "Type of nomenclature",
                "verbose_name_plural": "Type of nomenclatures",
            },
        ),
        migrations.CreateModel(
            name="Nomenclature",
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
                    "label",
                    models.CharField(max_length=255, verbose_name="Label"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True, verbose_name="Is active"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="child_nomenclature",
                        to="sinp_nomenclatures.nomenclature",
                        verbose_name="Parent nomenclature",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nomenclatures",
                        to="sinp_nomenclatures.type",
                        verbose_name="Type",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "nomenclatures",
                "unique_together": {("type", "code")},
            },
        ),
    ]

# Generated by Django 4.2.23 on 2025-07-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sinp_nomenclatures", "0003_nomenclature_parents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nomenclature",
            name="parents",
            field=models.ManyToManyField(
                blank=True,
                related_name="child_nomenclatures",
                to="sinp_nomenclatures.nomenclature",
                verbose_name="Parents nomenclature",
            ),
        ),
    ]

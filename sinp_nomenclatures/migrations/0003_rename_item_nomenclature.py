# Generated by Django 3.2.5 on 2021-08-10 20:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sinp_nomenclatures', '0002_alter_source_unique_together'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Nomenclature',
        ),
    ]
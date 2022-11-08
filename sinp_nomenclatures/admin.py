from django.contrib import admin

# Register your models here.
from .models import (
    Nomenclature,
    Type,
    Source,
)


class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "code", "label", "active")
    list_filter = ("type", "active")


# Register your models here.
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Type)
admin.site.register(Source)


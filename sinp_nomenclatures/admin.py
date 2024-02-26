from django.contrib import admin

# Register your models here.
from .models import Nomenclature, Source, Type


class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "code", "label", "active", "parent")
    list_filter = ("type", "active")


# Register your models here.
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Type)
admin.site.register(Source)

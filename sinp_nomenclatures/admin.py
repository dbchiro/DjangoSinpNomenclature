from django.contrib import admin
from django.utils.translation import gettext as _

# Register your models here.
from .models import Nomenclature, Source, Type


@admin.action(description=_("Mark selected items as active"))
def activate(_modeladmin, _request, queryset):
    """Set item active"""
    queryset.update(active=True)


@admin.action(description=_("Mark selected items as inactive"))
def inactivate(_modeladmin, _request, queryset):
    """Set item inactive"""
    queryset.update(active=False)


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "version",
        "url",
    )
    list_filter = ("name", "version")


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "mnemonic", "label", "status", "source")
    list_filter = (
        "source",
        "status",
    )


class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "code", "label", "active", "parent")
    list_filter = ("type", "active")
    actions = [activate, inactivate]


# Register your models here.
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Source, SourceAdmin)

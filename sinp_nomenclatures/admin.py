from django.contrib import admin
from django.utils.translation import gettext as _

# Register your models here.
from .models import Nomenclature, Source, Type


@admin.action(description=_("Mark selected items as enabled"))
def enabled(_modeladmin, _request, queryset):
    """Set item enabled"""
    queryset.update(status="ENABLED")


@admin.action(description=_("Mark selected items as disabled"))
def disabled(_modeladmin, _request, queryset):
    """Set item disabled"""
    queryset.update(status="DISABLED")


@admin.action(description=_("Mark selected items as hidden"))
def hidden(_modeladmin, _request, queryset):
    """Set item hidden"""
    queryset.update(status="HIDDEN")


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
    list_display = ("id", "type", "code", "label", "status")
    list_filter = ("type", "status")
    actions = [enabled, disabled, hidden]
    filter_horizontal = ('parents',)


# Register your models here.
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Source, SourceAdmin)

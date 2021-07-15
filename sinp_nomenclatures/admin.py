from django.contrib import admin

# Register your models here.
from .models import (
    Item,
    Type,
    Source,
)


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "code", "label", "active")
    list_filter = ("type", "active")


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Type)
admin.site.register(Source)


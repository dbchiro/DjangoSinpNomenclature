from django.urls import path

from .views import (
    NomenclatureViewset,
    SourceViewset,
    TypeViewset,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "sinp_nomenclatures"

router = DefaultRouter()

router.register(r'sources', SourceViewset,'sources')
router.register(r'types', TypeViewset, 'types')
router.register(r'nomenclatures', NomenclatureViewset, 'nomenclaturess')

urlpatterns = [
    path('', include(router.urls)),
    path(
        "nomenclatures/type/<int:pk>/item",
        TypeViewset.as_view({"get": "list"}),
        name="item_list",
    ),
    # path("nomenclature/type/<int:pk>/item/<int:pk>",TypeViewset.as_view({"get":"list"}), name="item_list"),
]

from django.urls import path

from .views import (
    NomenclatureViewset,
    SourceViewset,
    TypeViewset,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "sinp_nomenclatures"

router.register(r'sources', SourceViewset)
router.register(r'types', TypeViewset)
router.register(r'nomenclatures', NomenclatureViewset)

urlpatterns = [
    path('', include(router.urls))
    # path(
    #     "nomenclature/sources",
    #     SourceViewset.as_view({"get": "list"}),
    #     name="source_list",
    # ),
    # path(
    #     "nomenclature/source/<int:pk>",
    #     SourceViewset.as_view({"get": "retrieve"}),
    #     name="source",
    # ),
    # path(
    #     "nomenclature/types",
    #     TypeViewset.as_view({"get": "list"}),
    #     name="type_list",
    # ),
    # path(
    #     "nomenclature/type/<int:pk>",
    #     TypeViewset.as_view({"get": "retrieve"}),
    #     name="type",
    # ),
    # path(
    #     "nomenclature/type/<int:pk>/items",
    #     TypeViewset.as_view({"get": "list"}),
    #     name="item_list",
    # ),
    # path("nomenclature/type/<int:pk>/item/<int:pk>",TypeViewset.as_view({"get":"list"}), name="item_list"),
]

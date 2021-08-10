from django.urls import path

from .views import (
    NomenclatureViewset,
    SourceViewset,
    TypeViewset,
)


app_name = "sinp_nomenclatures"

urlpatterns = [
    path(
        "nomenclature/sources",
        SourceViewset.as_view({"get": "list"}),
        name="source_list",
    ),
    path(
        "nomenclature/source/<int:pk>",
        SourceViewset.as_view({"get": "retrieve"}),
        name="source",
    ),
    path(
        "nomenclature/types",
        TypeViewset.as_view({"get": "list"}),
        name="type_list",
    ),
    path(
        "nomenclature/type/<int:pk>",
        TypeViewset.as_view({"get": "retrieve"}),
        name="type",
    ),
    path(
        "nomenclature/type/<int:pk>/items",
        TypeViewset.as_view({"get": "list"}),
        name="item_list",
    ),
    # path("nomenclature/type/<int:pk>/item/<int:pk>",TypeViewset.as_view({"get":"list"}), name="item_list"),
]

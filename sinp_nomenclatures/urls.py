from django.urls import include, path
from rest_framework import routers

from .views import NomenclatureViewset, SourceViewset, TypeViewset

router = routers.SimpleRouter(trailing_slash=False)
app_name = "sinp_nomenclatures"


router.register(r"nomenclatures/sources", SourceViewset)
router.register(r"nomenclatures/types", TypeViewset)
router.register(r"nomenclatures/nomenclatures", NomenclatureViewset)

urlpatterns = [path("", include(router.urls))]

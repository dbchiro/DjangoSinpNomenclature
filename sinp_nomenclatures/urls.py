from django.urls import path

from .views import (
    NomenclatureViewset,
    SourceViewset,
    TypeViewset,
)
from django.urls import path, include

from rest_framework import routers

router = routers.SimpleRouter()
app_name = "sinp_nomenclatures"



router.register(r'sources', SourceViewset)
router.register(r'types', TypeViewset)
router.register(r'nomenclatures', NomenclatureViewset)

urlpatterns = [
    path('', include(router.urls))
]

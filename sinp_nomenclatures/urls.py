#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Django SINP Nomenclatures URLS"""


from django.urls import include, path
from rest_framework import routers

from .views import NomenclatureViewset, SourceViewset, TypeViewset

router = routers.SimpleRouter(trailing_slash=False)
app_name = "sinp_nomenclatures"


router.register(r"sources", SourceViewset)
router.register(r"types", TypeViewset)
router.register(r"nomenclatures", NomenclatureViewset)

urlpatterns = [path("", include(router.urls))]

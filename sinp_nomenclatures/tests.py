#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Django SINP Nomenclatures Tests"""


import datetime

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from rest_framework.test import APIRequestFactory

from sinp_nomenclatures.models import Source, Type
from sinp_nomenclatures.views import NomenclatureViewset

User = get_user_model()


class SourceTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="fred", email="fred@mydomain.net", password="top_secret"
        )

        Source.objects.create(
            name="Source1",
            version="v1.0.0",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
        )
        Source.objects.create(
            name="Source2",
            version="v1.1.2",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
        )

    def test_sources(self):
        """Source correctly created"""
        src1 = Source.objects.get(name="Source1")
        src2 = Source.objects.get(name="Source2")
        self.assertEqual(src1.version, "v1.0.0")
        self.assertEqual(src2.version, "v1.1.2")

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get("/api/v1/nomenclatures/nomenclatures")

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user
        # print(dir(request))
        # print(request.body)
        # # Or you can simulate an anonymous user by setting request.user to
        # # an AnonymousUser instance.
        # request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = NomenclatureViewset.as_view({"get": "list"})(request)
        self.assertEqual(response.status_code, 200)


class TypeTestCase(TestCase):
    def setUp(self):
        Source.objects.create(
            name="Source2",
            version="v1.1.2",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
        )
        Type.objects.create(
            code="type-test",
            mnemonic="test",
            label="TEST label",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
            source=Source.objects.get(name="Source2"),
        )

    def test_test(self):
        """Type correctly created"""
        typ = Type.objects.get(code="type-test")
        self.assertEqual(
            (typ.mnemonic, typ.source),
            ("test", Source.objects.get(name="Source2")),
        )


# Create your tests here.

# def test_version():
#     assert __version__ == "0.1.0"


# Using the standard RequestFactory API to create a form POST request
c = Client()
request = c.post(
    "/api/v1/nomenclatures/nomenclatures",
    {"code": "test", "mnemonic": "test", "label": "test", "type": 1},
)

print(request)

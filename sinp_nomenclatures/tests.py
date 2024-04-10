#!/usr/bin/env python3
"""Django SINP Nomenclatures Tests"""


import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

# from django.urls import reverse
from rest_framework.test import APIRequestFactory

from sinp_nomenclatures.models import Nomenclature, Source, Type
from sinp_nomenclatures.views import NomenclatureViewset, TypeViewset

User = get_user_model()


class SourceTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="fred",
            email="fred@mydomain.net",
            password="top_secret",
            is_superuser=True,
            is_staff=True,
        )
        Source.objects.create(
            name="Source1",
            version="v1.0.0",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
        )
        src2 = Source.objects.create(
            name="Source2",
            version="v1.1.2",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
        )
        typ1 = Type.objects.create(
            code="type-test",
            mnemonic="test",
            label="TEST label",
            create_date=datetime.datetime.now(),
            update_date=datetime.datetime.now(),
            source=src2,
        )
        self.nom_parent1 = Nomenclature.objects.create(
            type=typ1,
            code="nom1",
            label="Nomenclature 1",
            active=True,
        )
        self.nom_child1 = Nomenclature.objects.create(
            type=typ1,
            code="nom2",
            label="Nomenclature 2",
            active=True,
            parent=self.nom_parent1,
        )

    def test_sources(self):
        """Source correctly created"""
        src1 = Source.objects.get(name="Source1")
        src2 = Source.objects.get_by_natural_key("Source2", "v1.1.2")
        self.assertEqual(src1.version, "v1.0.0")
        self.assertEqual(src2.version, "v1.1.2")
        self.assertEqual(str(src1), f"{src1.name} ({src1.version})")
        self.assertEqual(
            src1.natural_key(),
            (
                src1.name,
                src1.version,
            ),
        )

    def test_type(self):
        """Type correctly created"""
        typ1 = Type.objects.get(code="type-test")
        self.assertEqual(
            (typ1.mnemonic, typ1.source),
            ("test", Source.objects.get(name="Source2")),
        )
        self.assertEqual(str(typ1), f"{typ1.code} - {typ1.mnemonic}")
        self.assertEqual(typ1.natural_key(), (typ1.code,))

    def test_nomenclature(self):
        """Type correctly created"""
        typ1 = Type.objects.get_by_natural_key("type-test")
        nom1 = Nomenclature.objects.get_by_natural_key(typ1.code, "nom1")
        self.assertEqual(str(nom1), nom1.label)
        self.assertEqual(nom1.natural_key(), ((nom1.type.code, nom1.code)))

    def test_details(self):
        print()
        # Create an instance of a GET request.
        r = self.factory.get("/")
        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        r.user = self.user
        # print(dir(request))
        # print(request.body)
        # # Or you can simulate an anonymous user by setting request.user to
        # # an AnonymousUser instance.
        # request.user = AnonymousUser()

        # Use this syntax for class-based views.
        response = NomenclatureViewset.as_view({"get": "list"})(r)
        self.assertEqual(response.status_code, 200)
        response = TypeViewset.as_view({"get": "list"})(r)
        self.assertEqual(response.status_code, 200)
        r = self.factory.get("/", QUERY_STRING="with_nomenclatures=true")
        r.user = self.user
        response = TypeViewset.as_view({"get": "list"})(r)
        self.assertEqual(response.status_code, 200)

    # def test_actions1(self):
    #     """
    #     Testing export_as_json action
    #     App is content_app, model is content
    #     modify as per your app/model
    #     """
    #     data = {
    #         "action": "activate",
    #         "_selected_action": [
    #             self.nom_parent1.pk,
    #             self.nom_child1.pk,
    #         ],
    #     }
    #     change_url = reverse(
    #         "admin:sinp_nomenclatures_nomenclature_changelist"
    #     )
    #     self.client.login(username="fred", password="top_secret")
    #     response = self.client.post(change_url, data)
    #     self.client.logout()
    #     print(dir(response))
    #     print(response.url)
    #     self.assertEqual(response.status_code, 200)


# class TypeTestCase(TestCase):
#     def setUp(self):
#         Source.objects.create(
#             name="Source2",
#             version="v1.1.2",
#             create_date=datetime.datetime.now(),
#             update_date=datetime.datetime.now(),
#         )
#         Type.objects.create(
#             code="type-test",
#             mnemonic="test",
#             label="TEST label",
#             create_date=datetime.datetime.now(),
#             update_date=datetime.datetime.now(),
#             source=Source.objects.get(name="Source2"),
#         )

#     def test_test(self):
#         """Type correctly created"""
#         typ = Type.objects.get(code="type-test")
#         self.assertEqual(
#             (typ.mnemonic, typ.source),
#             ("test", Source.objects.get(name="Source2")),
#         )
#         self.assertEqual(str(typ), f"{typ.code} - {typ.mnemonic}")
#         self.assertEqual(typ.natural_key(), (typ.code,))


# Create your tests here.

# def test_version():
#     assert __version__ == "0.1.0"


# Using the standard RequestFactory API to create a form POST request
# c = Client()
# request = c.post(
#     "/api/v1/nomenclatures/nomenclatures",
#     {"code": "test", "mnemonic": "test", "label": "test", "type": 1},
# )

# print(request)

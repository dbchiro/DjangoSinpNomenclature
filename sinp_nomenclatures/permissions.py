from django.conf import settings
from rest_framework.permissions import BasePermission


class IsOptionnalyAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if "NOMENCLATURE_API_IS_PUBLIC" in settings.__dict__:
            if settings.NOMENCLATURE_API_IS_PUBLIC:
                return True
        return bool(request.user and request.user.is_authenticated)

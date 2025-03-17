import logging

from django.conf import settings
from rest_framework.permissions import BasePermission

logger = logging.getLogger(__name__)


class IsOptionnalyAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    message = "Authentication required"

    def has_permission(self, request, view):
        """Check if API should be public or not"""
        is_public = getattr(settings, "NOMENCLATURE_API_IS_PUBLIC", False)
        if is_public:
            logger.debug(
                "<IsOptionnalyAuthenticated> API is public, no auth required"
            )
            return True
        is_authenticated = request.user and request.user.is_authenticated
        logger.debug(
            f"<IsOptionnalyAuthenticated> User authenticated: {is_authenticated}"
        )
        return is_authenticated

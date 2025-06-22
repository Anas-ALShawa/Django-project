from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsManagerOrReadOnly(BasePermission):
    """
    Allow read-only access to anyone,
    but write permissions only to users with is_staff=True (managers).
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS for everyone
        if request.method in SAFE_METHODS:
            return True

        # Otherwise, only allow if user is authenticated and is staff (manager)
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
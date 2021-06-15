from rest_framework import permissions


class IsOwnerOfObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.user == request.user
        else:
            return False


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated()):
            return True
        return False

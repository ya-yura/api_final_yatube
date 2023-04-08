from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Только владельцам объекта может редактировать его его."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

from rest_framework import permissions


class ProfielPermission(permissions.BasePermission):
    """
    プロフィールのパーミッション
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

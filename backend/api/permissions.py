from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
     Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    """
    The request is author as a user or the request is superuser as a user  , or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    """
    The request is Superuser as a user , or request is staff as a user has a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated and request.user.is_staff:
            return True
        return bool(
            request.user.is_authenticated and request.user.is_superuser 
        )


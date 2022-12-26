"""
Permissions file for the Note Model.
Prevents CRUD functionality on specific
items if the user is not the owner of the
Note.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission class for checking whether or not
    the user is the owner of the Note.
    """
    def has_object_permission(self, request, view, obj):
        """
        Function which takes the request, view and specific
        object and checks whether or not the user will be
        allowed CRUD capability.

        Parameters:
        request: Type of request.
        view: View used.
        object: Object checked against.

        Returns:
        bool
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.task.owner == request.user

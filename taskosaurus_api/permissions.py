"""
Permissions file used for everything other than the Note Model.
Allows or prevents CRUD functionality depending on the user's
current status. Used with the Profile and Task Models as they
both have ForeignKeys linked to a User instance.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission class for checking whether or not
    the user is the owner.
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
        return obj.owner == request.user


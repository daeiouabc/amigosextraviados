from rest_framework import permissions


class IsSelf(permissions.BasePermission):
    """
    Permiso customizado que solo permite que un usuario solo pueda ser mostado, editado o eliminado por el mismo
    """

    def has_object_permission(self, request, view, obj):
        """si el usuario que intenta acceder es el mismo"""
        return obj.id == request.user.id

from rest_framework import permissions


class IsSelf(permissions.BasePermission):
    """
    Permiso customizado que solo permite que un usuario solo pueda ser mostado, editado o eliminado por el mismo
    """

    def has_object_permission(self, request, view, obj):
        """si el usuario que intenta acceder es el mismo"""
        return obj.id == request.user.id


class IsAutor(permissions.BasePermission):
    """
    Permiso customizado
    """

    def has_object_permission(self, request, view, obj):
        """si el usuario que intenta acceder es el 'dueño' del objeto"""
        return obj.autor.id == request.user.id

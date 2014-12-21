from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """docstring for UsuarioSerializer, Clase para el CRUD"""

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'nombre', 'direccion', 'telefono', 'password')
        read_only_fields = ('id', )
        write_only_fields = ('password', )

    def update(self, attrs, instance=None):
        """metodo para asignar una nueva contraseña"""

        user = super(UsuarioSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

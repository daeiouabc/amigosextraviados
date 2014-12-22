from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """docstring for UsuarioSerializer, Clase para el CRUD"""
    #password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'is_active', 'nombre', 'apellido', 'direccion', 'telefono', 'password')
        read_only_fields = ('id', )
        #write_only_fields = ('password')#pending deprecation
        extra_kwargs = {'password': {'write_only': True}}

    #falta hacer que se pueda modificar el password
    """
    def update(self, instance, validated_data):
        #instance: usuario, validated_data: nuevos valores

        print("update")
        print(instance.password)
        user = super(UsuarioSerializer, self).update(instance, validated_data)
        #if instance.password:
        #    print("password")
        #    user.set_password(attrs['password'])
        return user
    """

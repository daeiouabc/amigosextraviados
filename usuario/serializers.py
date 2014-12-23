from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """UsuarioSerializer, Clase para el CRUD"""
    #password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'is_active', 'nombre', 'apellido', 'direccion', 'telefono', 'password')
        read_only_fields = ('id', )
        #write_only_fields = ('password')#pending deprecation
        extra_kwargs = {'password': {'write_only': True}}
        #password = serializers.Field(source='password', required=False)

    #falta hacer que se pueda modificar el password
    def update(self, instance, validated_data):
    #instance: usuario, validated_data: nuevos valores
        print("update")
        print(instance.password)
        user = super(UsuarioSerializer, self).update(instance, validated_data)
        #if instance.password:
        #    print("password")
        #    user.set_password(attrs['password'])
        return user


class UsuarioPublicoSerializer(serializers.ModelSerializer):
    """Usuario Publico Serializer, Clase para mostrar ls informacion del usuario al publico"""

    class Meta:
        model = Usuario
        fields = ('id', 'is_active', 'nombre', 'apellido')
        read_only_fields = ('id', 'is_active', 'nombre', 'apellido')

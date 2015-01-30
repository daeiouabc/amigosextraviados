from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """UsuarioSerializer, Clase para el CRUD"""
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'is_active', 'nombre', 'apellido', 'direccion', 'telefono', 'password')
        read_only_fields = ('id', 'is_active')
        #write_only_fields = ('password')#pending deprecation
        extra_kwargs = {'password': {'write_only': True}}
        #password = serializers.Field(source='password', required=False)

    def update(self, instance, validated_data):
        make_passwork = False
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        try:
            if validated_data.get('password', None):
                instance.password = validated_data.get('password', None)
                make_passwork = True
        except KeyError:
            print("No found")

        instance.update(make_passwork=make_passwork)
        return instance


class UsuarioPublicoSerializer(serializers.ModelSerializer):
    """Usuario Publico Serializer, Clase para mostrar ls informacion del usuario al publico"""
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta():
        model = Usuario
        fields = ('id', 'is_active', 'full_name')
        read_only_fields = ('id', 'is_active')

from rest_framework import serializers
from rest_framework.authtoken.models import Token


from usuario.models import Usuario


class UsuarioLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'email',
            'password',
        )


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = (
            'auth_token',
        )

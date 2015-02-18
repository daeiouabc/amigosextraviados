from rest_framework import generics, permissions, status, response
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .serializers import UsuarioLoginSerializer


class RootView(generics.GenericAPIView):
    """
    Root endpoint - use one of sub endpoints.
    """

    def get(self, request, format=None):
        urls_mapping = {
            'login': 'login',
            'logout': 'logout',
            'getToken': 'getToken',
            'delToken': 'delToken',
        }
        return Response({key: reverse(url_name, request=request, format=format)
                         for key, url_name in urls_mapping.items()})


from django.contrib.auth import authenticate, logout, login
from rest_framework import serializers

from . import constants


class LoginView(generics.GenericAPIView):
    """
    Login simple
    """
    serializer_class = UsuarioLoginSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            user = authenticate(email=request.DATA['email'], password=request.DATA['password'])
        except:
            raise serializers.ValidationError(constants.INCOMPLETE_CREDENTIALS)
        if user:
            if not user.is_active:
                raise serializers.ValidationError(constants.DISABLE_ACCOUNT_ERROR)
            else:
                return self.login(user)
        else:
            raise serializers.ValidationError(constants.INVALID_CREDENTIALS_ERROR)

    def login(self, user):
        login(self.request, user)
        return Response(status=status.HTTP_200_OK,)


class LogoutView(generics.GenericAPIView):
    """
    Logout simple
    """
    serializer_class = UsuarioLoginSerializer

    def delete(self, request):
        logout(request)
        return response.Response(status=status.HTTP_200_OK)

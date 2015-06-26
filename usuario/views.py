from rest_framework import viewsets, generics
from rest_framework.response import Response


from commons.permissions import IsSelf
from .serializers import UsuarioRegistroSerializer, UsuarioPublicoSerializer, UsuarioSerializer

from usuario.models import Usuario

from rest_framework.views import APIView


from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
User = get_user_model()


from rest_framework import permissions

from django.contrib.messages.views import SuccessMessageMixin


class CrearUsuario(viewsets.ModelViewSet,SuccessMessageMixin):
    """CrearUsuario, clase que se usa solo para crear un usuario"""
    serializer_class = UsuarioRegistroSerializer
    permission_classes = (permissions.AllowAny, )
    


class UsuarioViewSet(viewsets.ModelViewSet):
    """Usuario, clase con los metodos y rutas para el RUD"""
    serializer_class = UsuarioRegistroSerializer
    queryset = Usuario.objects.all()  # optimizar
    permission_classes = (IsSelf, )


class UsuarioPublico(APIView):
    """Muestra los datos publicos del usuario"""
    permission_classes = (permissions.AllowAny, )
    serializer_class = UsuarioPublicoSerializer

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UsuarioPublicoSerializer(user)
        return Response(serializer.data)


class Usuario(APIView):
    """Usuario, clase para mostar toda la info del usuario que se encuentra autenticado"""
    permission_classes = (IsSelf, permissions.IsAuthenticated)

    def get(self, request):
        user = request.user
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

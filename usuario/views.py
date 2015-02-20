from rest_framework import viewsets, generics
from rest_framework.response import Response


from commons.permissions import IsSelf
from .serializers import UsuarioRegistroSerializer, UsuarioPublicoSerializer, UsuarioSerializer

from .models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    """Usuario, clase con los metodos y rutas para el RUD"""
    serializer_class = UsuarioRegistroSerializer
    queryset = Usuario.objects.all()  # optimizar
    permission_classes = (IsSelf, )


from rest_framework import permissions


class CrearUsuario(viewsets.ModelViewSet):
    """CrearUsuario, clase que se usa solo para crear un usuario"""
    serializer_class = UsuarioRegistroSerializer
    permission_classes = (permissions.AllowAny, )


from rest_framework.views import APIView


class UsuarioPublico(APIView):
    """Usuario, clase con los metodos y rutas para mostrar los datos publicos del usuario"""
    permission_classes = (permissions.AllowAny, )

    def get(self, request, pk):
        user = Usuario.objects.all()
        serializer = UsuarioPublicoSerializer(user, many=Truem)
        return Response(serializer.data)


class Usuario(APIView):
    """Usuario, clase para mostar toda la info del usuario que se encuentra autenticado"""
    permission_classes = (IsSelf, permissions.IsAuthenticated)

    def get(self, request):
        user = request.user
        serializer = UsuarioSerializer(user)
        return Response(serializer.data)

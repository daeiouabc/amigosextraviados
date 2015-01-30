from rest_framework import viewsets


from django.contrib.auth import get_user_model


from commons.permissions import IsSelf
from .serializers import UsuarioSerializer, UsuarioPublicoSerializer


#para obtener la clase que se usa para la autenticacion
Usuario = get_user_model()
from commons.permissions import AuthMixin


class UsuarioViewSet(AuthMixin, viewsets.ModelViewSet):
    """Usuario, clase con los metodos y rutas para el RUD"""
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()  # optimizar
    permission_classes = (IsSelf, )


class CrearUsuario(viewsets.ModelViewSet):
    """CrearUsuario, clase que se usa solo para crear un usuario"""
    serializer_class = UsuarioSerializer
    permission_classes = ()


from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UsuarioPublico(AuthMixin, APIView):
    """Usuario, clase con los metodos y rutas para mostrar los datos publicos del usuario"""

    def get(self, request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioPublicoSerializer(user)
        return Response(serializer.data)

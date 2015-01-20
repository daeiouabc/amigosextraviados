from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model


from commons.permissions import IsSelf
from .serializers import UsuarioSerializer, UsuarioPublicoSerializer
from .models import Usuario


"""para sacar la clase que se usa para la autenticacion"""
#Usuario = get_user_model()


class UsuarioViewSet(viewsets.ModelViewSet):
    """Usuario, clase con los metodos y rutas para el RUD"""
    model = Usuario
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()  # optimizar
    permission_classes = (IsAuthenticated, IsSelf)


class CrearUsuario(viewsets.ModelViewSet):
    """CrearUsuario, clase que se usa solo para crear un usuario"""
    model = Usuario
    serializer_class = UsuarioSerializer


from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UsuarioPublico(APIView):
    """Usuario, clase con los metodos y rutas para mostrar los datos publicos del usuario"""
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioPublicoSerializer(user)
        return Response(serializer.data)


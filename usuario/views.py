from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model


from commons.permissions import IsSelf
from .serializers import UsuarioSerializer


"""para sacar la clase que se usa para la autenticacion"""
Usuario = get_user_model()


class Usuario(viewsets.ModelViewSet):
    """Usuario, clase con los metodos y rutas para el CRUD"""
    model = Usuario
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()  # optimizar
    permission_classes = (IsAuthenticated, IsSelf)


class CrearUsuario(viewsets.ModelViewSet):
    """CrearUsuario, clase que se usa solo para crear un usuario"""
    model = Usuario
    serializer_class = UsuarioSerializer

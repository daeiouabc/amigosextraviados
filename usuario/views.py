from rest_framework import viewsets, permissions

from django.contrib.auth import get_user_model
from commons.permissions import IsOwner
from .serializers import UsuarioSerializer

#para sacar la clase que se usa para la autenticacion
Usuario = get_user_model()


class Usuario(viewsets.ModelViewSet):
    """Usuario, clase con los metodos y rutas para el CRUD"""
    model = Usuario
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.order_by(Usuario.USERNAME_FIELD)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

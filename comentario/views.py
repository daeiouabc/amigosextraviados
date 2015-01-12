from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Comentario
from .serializers import ComentarioSerializer

from commons.permissions import IsAutor


class ComentarioViewSet(viewsets.ModelViewSet):
    """ComentarioViewSet, clase con los metodos y rutas para el RUD"""
    model = Comentario
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()
    permission_classes = (IsAuthenticated, IsAutor)


class CrearComentario(viewsets.ModelViewSet):
    """CrearComentario, clase que se usa solo para crear un Comentario"""
    model = Comentario
    serializer_class = ComentarioSerializer
    permission_classes = (IsAuthenticated,)

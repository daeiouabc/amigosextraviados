from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Comentario
from .serializers import ComentarioSerializer, ComentarioPublicoSerializer

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


from rest_framework.generics import ListAPIView


class ComentarioLista(ListAPIView):
    serializer_class = ComentarioPublicoSerializer
    paginate_by = 5

    def get_queryset(self):
        print(self.kwargs['pk'])
        return Comentario.objects.filter(object_id=self.kwargs['pk'])

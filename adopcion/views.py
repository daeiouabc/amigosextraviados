from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Adopcion
from .serializer import AdopcionSerializer, AdopcionShortSerializer


class AdopcionViewSet(viewsets.ModelViewSet):
    """Clase para Editar, Eliminar"""
    model = Adopcion
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionSerializer


class CreateAdopcion(viewsets.ModelViewSet):
    """Clase para crear una mascota en Adopcion"""
    model = Adopcion
    serializer_class = AdopcionSerializer
    permission_classes = (IsAuthenticated, )


class AdopcionLista(ListModelMixin, viewsets.GenericViewSet):
    #Listado de solo lectura de mascotas en adopcion
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionShortSerializer
    permission_classes = (AllowAny, )

    def list(self, request, *args, **kwargs):
        query = Adopcion.objects.all()

        #instance = self.filter_queryset(query)
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(query, many=True)
        return Response({'adopciones': serializer.data})

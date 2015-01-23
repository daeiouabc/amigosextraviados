from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Perdido
from .serializer import PerdidoSerializer, PerdidoShortSerializer


class PerdidoViewSet(viewsets.ModelViewSet):
    """docstring for ClassName"""
    model = Perdido
    queryset = Perdido.objects.all()
    serializer_class = PerdidoSerializer


class CreatePerdido(viewsets.ModelViewSet):
    """docstring for CreatePerdido"""
    model = Perdido
    serializer_class = PerdidoSerializer
    permission_classes = (IsAuthenticated, )


from .filters import PerdidoFilter
from rest_framework import filters

from rest_framework.response import Response
#from rest_framework import status
from django.contrib.auth import get_user_model
Usuario = get_user_model()


#from usuario.serializers import UsuarioPublicoSerializer
from rest_framework import mixins


class PerdidoCercanoLista(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Listado de solo lectura de perdidos cercanos a la ubicacion del Usuario, tambien provee filtro por especie"""
    queryset = Perdido.objects.all()
    serializer_class = PerdidoShortSerializer
    filter_class = PerdidoFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter, )
    search_fields = ('especie', )

    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        #query = Perdido.objects.filter(dirDesaparicion=request.user.direccion)
        query = Perdido.objects.filter(dirDesaparicion__contains=request.user.direccion)

        instance = self.filter_queryset(query)
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

"""
class PerdidoLista(mixins.ListModelMixin, viewsets.GenericViewSet):
    #Listado de solo lectura de perdidoss
    queryset = Perdido.objects.all()
    serializer_class = PerdidoSerializer
    filter_class = PerdidoFilter
    search_fields = ('especie', )
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter, )

    def get_queryset(self):
        return Perdido.objects.all()

    def info(self, request, pk=None):
        autor = Usuario.objects.get(pk=self.get_object().autor.id)
        serializado = UsuarioPublicoSerializer(autor, many=False)
        return Response(serializado.data, status=status.HTTP_200_OK)
"""

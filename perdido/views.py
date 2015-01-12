from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Perdido
from .serializer import PerdidoSerializer



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
		
		
from rest_framework import serializers
from .models import Perdido


class PerdidoSerializer(serializers.ModelSerializer):
    """docstring for PerdidoSerializer"""
    class Meta:
        model = Perdido

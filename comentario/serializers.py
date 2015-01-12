from rest_framework import serializers
from .models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    """ComentarioSerilizer"""

    class Meta:
        model = Comentario
        read_only_fields = ('id', 'fechaPublicacion', 'autor')

    def create(self, validated_data):
        validated_data['autor'] = self.context['request'].user
        return Comentario.objects.create(**validated_data)

from rest_framework import serializers
from comentario.models import Comentario

from .models import Adopcion


class AdopcionSerializer(serializers.ModelSerializer):
    """Clase para crear una mascota en Adopcion"""
    class Meta:
        model = Adopcion
        fields = ('nombre', 'especie', 'raza', 'sexo', 'descripcion', 'position', 'photo', 'dirContacto')


class AdopcionShortSerializer(serializers.ModelSerializer):
    """La minima info sobre una mascota"""
    thumb = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Adopcion
        fields = ('id', 'nombre', 'thumb', 'dirContacto', 'adoptado', 'fechaPublicacion', 'comments_count')

    def get_thumb(self, object):
        try:
            return object.photo['medio'].url
        except:
            #poner algo menos feo XD
            return "No found"

    def get_comments_count(self, object):
        return Comentario.objects.filter(object_id=object.id).count()

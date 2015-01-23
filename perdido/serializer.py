from rest_framework import serializers
from .models import Perdido


class PerdidoSerializer(serializers.ModelSerializer):
    """docstring for PerdidoSerializer"""
    class Meta:
        model = Perdido


from comentario.models import Comentario


class PerdidoShortSerializer(serializers.ModelSerializer):
    """docstring for PerdidoSerializer"""
    thumb = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Perdido
        fields = ('id', 'nombre', 'thumb', 'comments_count')

    def get_thumb(self, object):
        try:
            return object.photo['medio'].url
        except:
            #poner algo menos feo XD
            return "No found"

    def get_comments_count(self, object):
        return Comentario.objects.filter(object_id=object.id).count()

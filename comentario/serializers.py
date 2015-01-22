from rest_framework import serializers
from .models import Comentario
from notifications import notify

from perdido.models import Perdido


class ComentarioSerializer(serializers.ModelSerializer):
    """ComentarioSerializer"""

    class Meta:
        model = Comentario
        read_only_fields = ('id', 'fechaPublicacion', 'autor', )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['autor'] = user
        return Comentario.objects.create(**validated_data)

    def save(self):
        super(ComentarioSerializer, self).save()
        actor = self.context['request'].user
        verb = 'Comentado'
        action_object = self.instance
        target = Perdido.objects.get(pk=self.instance.object_id)
        recipient = target.autor
        notify.send(actor, recipient=recipient, action_object=action_object, verb=verb, target=target, description=action_object.texto)


from usuario.serializers import UsuarioPublicoSerializer


class ComentarioPublicoSerializer(serializers.ModelSerializer):
    autor = serializers.SerializerMethodField()

    class Meta:
        model = Comentario
        fields = ('id', 'fechaPublicacion', 'texto', 'autor')

    def get_autor(self, object):
        autor = UsuarioPublicoSerializer(object.autor)
        return autor.data

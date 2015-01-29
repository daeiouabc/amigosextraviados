from rest_framework import serializers
from .models import Comentario
from notifications import notify

from perdido.models import Perdido

from django.contrib.contenttypes.models import ContentType


class ComentarioSerializer(serializers.ModelSerializer):
    """ComentarioSerializer"""

    class Meta:
        model = Comentario
        read_only_fields = ('id', 'fechaPublicacion', 'autor', )

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['autor'] = user

        if validated_data['publicacion_type'] == ContentType.objects.get_for_model(Perdido):
            print("Perdido")

        validated_data['object_id']
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

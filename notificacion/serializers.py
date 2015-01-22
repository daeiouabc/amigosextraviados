from rest_framework import serializers
from notifications.models import Notification

from usuario.models import Usuario
from usuario.serializers import UsuarioPublicoSerializer


from django.contrib.contenttypes.models import ContentType

from perdido.models import Perdido
from perdido.serializer import PerdidoSerializer

from comentario.models import Comentario
from comentario.serializers import ComentarioPublicoSerializer


class NotificationSerializer(serializers.ModelSerializer):
    """Notification"""
    actor_object = serializers.SerializerMethodField()
    target_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id',  # id de la notificacion
            'level',  # tipo de notificaion (info, error, warning....)
            'unread',  # leido o no
            'verb',  # accion
            'timestamp',  # hora que se poduce la notificacion
            'actor_object',  # actor que dispara la notificacion
            'target_object',  # objeto sobre el cual se produce la notificacion
            'description',)

    def get_actor_object(self, object):
        """
        Obtiene el usuario que genero la notificacion, lo serializa y retorna el JSON
        """
        return UsuarioPublicoSerializer(Usuario.objects.get(pk=object.actor_object_id)).data

    def get_target_object(self, object):
        """
        Obtiene el objeto (Perdido, Ado.....) sobre el cual fue realizada la accion, lo serializa y retorna el JSON
        """
        if object.target_content_type == ContentType.objects.get_for_model(Perdido):
            target = PerdidoSerializer(Perdido.objects.get(pk=object.target_object_id))

        elif object.target_content_type == ContentType.objects.get_for_model(Comentario):
            """
            NOTA: se pone Comentario para efectos de test, mientras se implementan las clases para Adoptado, etc
            """
            target = ComentarioPublicoSerializer(Comentario.objects.get(pk=object.target_object_id))

        # retorna el JSON del target
        return target.data

#Tipo de accion de ejecuta
#action_object_content_type (Perdido, Comentario, Usuario, .....)
#action_object_object_id

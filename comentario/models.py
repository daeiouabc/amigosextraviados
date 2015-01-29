from commons.publicacion import Publicacion
from django.db import models


from usuario.models import Usuario

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
#from perdido.models import Perdido


class Comentario(Publicacion, models.Model):
    texto = models.CharField(max_length=300)
    """
    CHOISES = (
        (ContentType.objects.get_for_model(Perdido), 'PERDIDO'),
        )
    publicacion_type = models.ForeignKey(ContentType, choises=CHOISES, null=False)
    """
    publicacion_type = models.ForeignKey(ContentType, null=False)
    object_id = models.PositiveIntegerField(null=False, )
    content_object = generic.GenericForeignKey("publicacion_type", "object_id")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.texto

    def get_full_name_autor(self):
        return u'%s' % Usuario.objects.get(pk=self.autor.id).get_full_name()

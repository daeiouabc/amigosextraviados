from commons.publicacion import Publicacion
from django.db import models


from usuario.models import Usuario

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Comentario(Publicacion, models.Model):
    texto = models.CharField(max_length=300)
    #publicacion_type = models.ForeignKey(ContentType, null=False)
    object_id = models.PositiveIntegerField(null=False, )
    #content_object = generic.GenericForeignKey("publicacion_type", "object_id")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.texto

    def get_full_name_autor(self):
        return u'%s' % Usuario.objects.get(pk=self.autor.id).get_full_name()

    """
    def save(self, *args, **kwargs):
        print("save")
        if not self.publicacion:
            self.publicacion = ContentType.objects.get_for_model(self.__class__)
            super(Comentario, self).save(*args, **kwargs)
    """
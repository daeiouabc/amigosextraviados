from django.db import models
from .publicacion import Publicacion

from geoposition.fields import GeopositionField
from easy_thumbnails.fields import ThumbnailerImageField

#from django.contrib.contenttypes import generic
#from django.contrib.contenttypes.models import ContentType

from django.utils import timezone
import re

from django.conf import settings


def content_file_name(instance, filename):
    out_file = str(instance.id) + "".join([c for c in str(timezone.now()) if re.match(r'\w', c)])
    return '/'.join(['mascotas', str(instance.autor.id), out_file])


class Mascota(Publicacion):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=400, verbose_name="Descripcion")
    position = GeopositionField(blank=True)
    photo = ThumbnailerImageField(upload_to=content_file_name, resize_source=settings.DEFAULT_MASCOTA_IMAGE_SETTING, blank=True)

    # Generic FK to the object
    #content_type = models.ForeignKey(ContentType)
    #object_id = models.PositiveIntegerField()
    #content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return u'%s %s' % (self.id, self.nombre)

    class Meta:
        abstract = True

from django.db import models
from .publicacion import Publicacion

from geoposition.fields import GeopositionField

#from django.contrib.contenttypes import generic
#from django.contrib.contenttypes.models import ContentType


class Mascota(Publicacion):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=400, verbose_name="Descripcion")
    position = GeopositionField(blank=True)

    # Generic FK to the object
    #content_type = models.ForeignKey(ContentType)
    #object_id = models.PositiveIntegerField()
    #content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return u'%s %s' % (self.id, self.nombre)

    class Meta:
        abstract = True

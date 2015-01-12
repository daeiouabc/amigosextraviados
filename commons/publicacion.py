from django.db import models
from django.conf import settings


class Publicacion(models.Model):
    """Publicacion: Clase Abstacta la cuall contiene los atributos que son comunes a una publicacion"""
    #settings.AUTH_USER_MODEL, para la modularidad
    #Nota: El autor no puede ser editable
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    fechaPublicacion = models.DateTimeField('publicado el', auto_now_add=True)

    class Meta:
        abstract = True

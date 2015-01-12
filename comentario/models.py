from commons.publicacion import Publicacion
from django.db import models


class Comentario(Publicacion):
    texto = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.texto

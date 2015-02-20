from django.db import models
from commons.mascota import Mascota


class Perdido(Mascota):
    fechaDesaparicion = models.DateField()
    dirDesaparicion = models.CharField(max_length=60)
    encontrado = models.BooleanField(default=False)

    def pre_save(self, obj):
        obj.autor.id = self.request.user

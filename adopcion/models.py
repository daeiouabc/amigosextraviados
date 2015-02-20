from django.db import models
from commons.mascota import Mascota


class Adopcion(Mascota):
    dirContacto = models.CharField(max_length=60)
    adoptado = models.BooleanField(default=False)

    def pre_save(self, obj):
        obj.autor.id = self.request.user

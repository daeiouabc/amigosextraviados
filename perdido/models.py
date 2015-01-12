from django.db import models
from commons.mascota import Mascota


class Perdido(Mascota):
	fechaDesaparicion = models.DateField()
	dirDesaparicion = models.CharField(max_length=50)


	def pre_save(self, obj):
		print ("pre save")
		obj.usuario = self.request.user
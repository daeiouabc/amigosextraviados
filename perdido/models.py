from django.db import models
from commons.mascota import Mascota
from usuario.models import Usuario



class Perdido(Mascota):
	usuario = models.ForeignKey(Usuario, editable=False)
	fechaDesaparicion = models.CharField(max_length=15, help_text='AAAA/MM/DD')
	dirDesaparicion = models.CharField(max_length=50)

	
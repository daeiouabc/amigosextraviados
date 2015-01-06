from django.db import models


class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	especie = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=400, verbose_name="Descripcion")
	fechaPublicacion = models.DateField(auto_now=True, editable=False)

	def __unicode__(self):
		return u'%s %s' % (self.id, self.nombre)

	class Meta:
		abstract = True
			
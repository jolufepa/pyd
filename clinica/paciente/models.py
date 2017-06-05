from django.db import models

# Create your models here.
class modelPaciente(models.Model):
	nombre = models.CharField('nombre', max_length=50)
	apellido_paterno = models.CharField('apellido_paterno', max_length=50)
	apellido_materno = models.CharField('apellido_materno', max_length=50)
	dni = models.CharField('dni', max_length=50)
	fecha_nacimiento = models.DateField('fecha de nacimiento')
	direccion = models.CharField('direccion', max_length=50)
	telefono_fijo = models.IntegerField(blank=True, null=True)
	telefono_movil = models.IntegerField()
	email = models.EmailField()
	fecha_alta = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.dni
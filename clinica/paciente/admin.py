from django.contrib import admin

# Register your models here.
from .models import modelPaciente
class adminPaciente(admin.ModelAdmin):
	list_display = ['dni', 'apellido_paterno', 'apellido_materno', 'telefono_movil','fecha_nacimiento', 'fecha_alta']
	class Meta:
		model = modelPaciente

admin.site.register(modelPaciente, adminPaciente)

from django import forms
from .models import modelPaciente
class formPaciente(forms.Form):
	nombre = forms.CharField()
	apellido_paterno = forms.CharField()
	apellido_materno = forms.CharField()
	dni = forms.CharField()
	fecha_nacimiento = forms.DateField(label=u'fecha de nacimiento', input_formats=['%d/%m/%Y', '%m/%d/%Y',], required=False, widget=forms.DateInput(format = '%d/%m/%Y'))
	direccion = forms.CharField()
	telefono_fijo = forms.IntegerField()
	telefono_movil = forms.IntegerField()
	email = forms.EmailField()

	def clean_dni(self):
		form_dni =  self.cleaned_data['dni']
		qs = modelPaciente.objects.filter(dni=form_dni)
		if qs.exists():
			raise forms.ValidationError("Error el dni ya existe")
		return form_dni	

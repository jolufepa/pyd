from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .form import formPaciente
from .models import modelPaciente


def index(request):
	return render(request, "index.html", {})


def registro(request):
	form = formPaciente(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get('nombre')
		abc1 = form_data.get('apellido_paterno')
		abc2 = form_data.get('apellido_materno')
		abc3 = form_data.get('dni')
		abc4 = form_data.get('fecha_nacimiento')
		abc5 = form_data.get('direccion')
		abc6 = form_data.get('telefono_fijo')
		abc7 = form_data.get('telefono_movil')
		abc8 = form_data.get('email')
		obj = modelPaciente.objects.create(nombre=abc.title(), apellido_paterno=abc1.title(), apellido_materno=abc2.title(), 
			dni=abc3.upper(), fecha_nacimiento=abc4, direccion=abc5, telefono_fijo=abc6, telefono_movil=abc7, email=abc8.lower())

		return HttpResponseRedirect("/registro?")
	context = {
		"el_form":form
	}	

	return render(request, 'registro.html', context)
	
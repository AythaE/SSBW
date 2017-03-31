# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse, redirect, render

from .forms import RestaurantesForm
# El punto se refiere al directorio de este archivo
from .models import addr, restaurants


# Create your views here.

# 2 Funcuones correspondientes al enrutador "urls.py"


def index(request):
  ultimosRestaurants = list(reversed(
      restaurants.objects[len(restaurants.objects) - 25:len(restaurants.objects)]))
  context = {
      'resta': ultimosRestaurants,
  }
  return render(request, 'home.html', context)


def test(request):

  context = {
      'variable': 3,
      'resta': restaurants.objects(cuisine='Granaina'),
  }   # Aquí van la las variables para la plantilla
  return render(request, 'test.html', context)


def buscar(request):
  cocina = request.GET.get('cocina')
  lista = restaurants.objects(cuisine__icontains=cocina)

  context = {
      'resta': lista,
      'busqueda': cocina,
  }
  return render(request, 'buscar.html', context)


def add(request):
  formu = RestaurantesForm()

  if request.method == "POST":

    formu = RestaurantesForm(request.POST, request.FILES)
    if formu.is_valid():                    # valida o añade errores

      # datos sueltos

      nombre = formu.cleaned_data['nombre']
      cocina = formu.cleaned_data['cocina']
      barrio = formu.cleaned_data['barrio']
      calle = formu.cleaned_data['dirección']

      # Revisar si esto funciona así
      imagen = formu.cleaned_data['imagen']

      tipo_foto = imagen.content_type
      # Para guardar tipo de archivo y nombre
      direc = addr(street=calle)
      i = image(extension=tipo_foto, img=imagen)
      r = restaurants(name=nombre, cuisine=cocina,
                      borough=barrio, address=direc, image=imagen)

      r.save()

      # formu.save()                         # si está ligado al model

      return redirect(index)
  # GET o error
  context = {
      'form': formu,
  }
  return render(request, 'aniadir.html', context)

# Sacar campo name poniendo () en url.py


def restaurante(request, name):
  resta =

  context = {
      'resta': resta,
  }
  return render(request, 'restaurante.html', context)


# /restaurante/nombreRest/imagen/
def imagen(request, nombreResta):

  res = restaurants.object(name=nombreResta)

  img = res.image.read()

  return HttpResponse(img, content_type="image")

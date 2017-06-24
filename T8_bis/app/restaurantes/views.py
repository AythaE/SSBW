# -*- coding: utf-8 -*-
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render

from .forms import RestaurantesForm
# El punto se refiere al directorio de este archivo
from .models import addr, image, restaurants

logger = logging.getLogger(__name__)
# Create your views here.

# 2 Funcuones correspondientes al enrutador "urls.py"


def index(request):
  logger.info("Index")
  restaurantes = restaurants.objects
  ultimosRestaurants = list(reversed(
      restaurantes[len(restaurantes) - 10:len(restaurantes)]))
  context = {
      'resta': ultimosRestaurants,
      'menu': "nav-listar",

  }
  return render(request, 'home.html', context)


def test(request):

  context = {
      'variable': 3,
      'resta': restaurants.objects(cuisine='Granaina'),
  }   # Aquí van la las variables para la plantilla
  return render(request, 'test.html', context)


@login_required
def buscar(request):
  cocina = request.GET.get('cocina')
  logger.info("Buscando restaurantes de cocina: " + str(cocina))

  lista = restaurants.objects(cuisine__icontains=cocina)

  context = {
      'resta': lista,
      'busqueda': cocina,
  }
  return render(request, 'buscar.html', context)


@login_required
def add(request):
  formu = RestaurantesForm()

  if request.method == "POST":

    formu = RestaurantesForm(data=request.POST)
    if formu.is_valid():                    # valida o añade errores
      print(formu.cleaned_data)
      # datos sueltos

      nombre = formu.cleaned_data['nombre']
      cocina = formu.cleaned_data['cocina']
      barrio = formu.cleaned_data['barrio']
      calle = formu.cleaned_data['dirección']
      logger.info("Añadiendo restaurante: " + str(nombre))

      # Revisar si esto funciona así
      imagen = request.FILES.get('imagen')
      tipo_foto = imagen.content_type
      # Para guardar tipo de archivo y nombre
      direc = addr(street=calle)
      i = image(extension=tipo_foto, img=imagen)
      r = restaurants(name=nombre, cuisine=cocina,
                      borough=barrio, address=direc, image=i)

      r.save()

      # formu.save()                         # si está ligado al model

      return redirect(index)
  # GET o error
  context = {
      'form': formu,
      'menu': "nav-add",
  }
  return render(request, 'aniadir.html', context)

# Sacar campo name poniendo () en url.py


@login_required
def restaurante(request, name):
  logger.info("Mostrando restaurante: " + name)

  resta = restaurants.objects(name__exact=name)[0]

  context = {
      'resta': resta,
  }
  return render(request, 'restaurante.html', context)


# /restaurante/nombreRest/imagen/


@login_required
def imagen(request, name):

  res = restaurants.objects(name__exact=name)[0]
  logger.info("Recuperando imagen del restaurante: " + res.name)

  img = res.image.img.read()

  content_type = res.image.extension

  return HttpResponse(img, content_type=content_type)

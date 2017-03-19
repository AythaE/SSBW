from django.shortcuts import HttpResponse, render

# El punto se refiere al directorio de este archivo
from .models import restaurants


# Create your views here.

# 2 Funcuones correspondientes al enrutador "urls.py"


def index(request):
  context = {
      'resta': restaurants.objects[:100],
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

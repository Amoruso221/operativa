from django.shortcuts import render
from vacunatorios.models import Sede

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sedes(request):
    sedes = Sede.objects.all()
    return render(request, 'sedes.html', {'sedes': sedes})


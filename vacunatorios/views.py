from django.shortcuts import render
from vacunatorios.models import Sede

# Create your views here.


def all_sedes(request):
    sedes = Sede.objects.all()
    return render(request,
                  'vacunatorios/sedes.html',
                  {'sedes': sedes}
                  )


def index(request):
    return render(request, 'index.html')


def sedes(request):
    return render(request, 'sedes.html')


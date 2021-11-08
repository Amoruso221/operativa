from django.shortcuts import render
from vacunatorios.models import Sede
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def estado_actual(hora_inicio, hora_fin):
    ahora = datetime.now().time()
    estado = "cerrado"

    if ahora > hora_inicio and ahora < hora_fin:
        estado = "abierto"
    return estado


def sedes(request):
    sedes = Sede.objects.all()

    for sede in sedes:
        sede.estado = estado_actual(sede.hora_inicio, sede.hora_fin)

    return render(request, 'sedes.html', {'sedes': sedes})

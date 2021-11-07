from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vacunatorios.models import Sede
from datetime import datetime
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
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
        promedio = tiempo_promedio(sede.longitud_cola)

    return render(request, 'sedes.html', {'sedes': sedes, 'promedio': promedio})


def tiempo_promedio(longitud_cola):
    # Lc/λ
    # Longitud de la cola/ promedio de llegadas
    llegadas = 4
    res = longitud_cola / llegadas
    return res

@login_required
def sede_logeada(request):
    return render(request, 'sedeLogeada.html')


def logout_view(request):

    logout(request, 'index.html')




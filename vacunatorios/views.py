import math

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vacunatorios.models import Sede
from datetime import datetime
from django.contrib.auth import logout
import random
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
        promedio = promedio_tiempo_espera(sede.prom_llegadas, sede.prom_atendidas)

    return render(request, 'sedes.html', {'sedes': sedes, 'promedio': promedio})



def promedio_tiempo_espera(prom_llegadas, prom_atendidas):
    #Prom. de llegadas / tiempo
    v_lambda = prom_llegadas / 60
    #Prom. de unidades atendidas / tiempo
    mu = prom_atendidas / 60
    # Lc/λ
    # Lc = Prom. de unidades en espera / Longitud de la cola

    lc = (v_lambda * v_lambda) / (mu * (mu - v_lambda))
    resultado = lc / v_lambda

    return resultado

@login_required
def sede_logeada(request):

    sedes = Sede.objects.all()

    for sede in sedes:
        if sede.user == request.user:
            sede.estado = estado_actual(sede.hora_inicio, sede.hora_fin)
            promedio = promedio_tiempo_espera(sede.prom_llegadas, sede.prom_atendidas)
            return render(request, 'sedeLogeada.html', {'sede': sede, 'promedio': promedio})


def logout_view(request):

    logout(request, 'index.html')


<<<<<<< HEAD
    return render(request, 'sedes.html', {'sedes': sedes})
=======

>>>>>>> agustin

from django.db import models
<<<<<<< HEAD

=======
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
>>>>>>> agustin
# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField(default=0)
    vacuna = models.CharField(max_length=50)
    hora_inicio = models.TimeField(default=datetime.time(9, 00))
    hora_fin = models.TimeField(default=datetime.time(17, 00))
    prom_llegadas = models.FloatField(default=0.0)
    prom_atendidas = models.FloatField(default=0.0)
    longitud_cola = models.IntegerField(default=0)
    habilitada = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="img/%y", default="default.svg")
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
<<<<<<< HEAD
        txt = "Nombre: {0}, Direccion: {1} {2}, Vacuna: {3}, Canales: {4}, Espera maxima (mins): {5}"
        return txt.format(self.nombre, self.calle, self.numero, self.vacuna, self.canales, self.espera_maxima)
=======
        txt = "Nombre: {0}, Direccion: {1} {2}, Vacuna: {3}, Canales: {4}, Espera maxima (mins): {5}, User: {6}"
        return txt.format(self.nombre, self.calle, self.numero, self.vacuna, self.canales, self.espera_maxima, self.user)


>>>>>>> agustin

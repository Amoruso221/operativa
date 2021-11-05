from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField(default=0)
    vacuna = models.CharField(max_length=50)
    canales = models.IntegerField(default=0)
    espera_maxima = models.IntegerField(default=0)
    longitud_cola = models.IntegerField(default=0)
    abierta = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="img/%y", default="default.svg")

    def __str__(self):
        txt = "Nombre: {0}, Direccion: {1} {2}, Vacuna: {3}, Canales: {4}, Espera maxima (mins): {5}"
        return txt.format(self.nombre, self.calle, self.numero, self.vacuna, self.canales, self.espera_maxima)

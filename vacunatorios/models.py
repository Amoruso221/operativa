from django.db import models

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    vacuna = models.CharField(max_length=50)
    abierta = models.BooleanField(default=True)
    canales = models.IntegerField()



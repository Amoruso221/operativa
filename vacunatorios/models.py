from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    vacuna = models.CharField(max_length=50)
    abierta = models.BooleanField(default=True)
    canales = models.IntegerField()
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

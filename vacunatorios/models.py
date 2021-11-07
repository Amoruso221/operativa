from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField(default=0)
    vacuna = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    canales = models.IntegerField(default=0)
    espera_maxima = models.IntegerField(default=0)
    longitud_cola = models.IntegerField(default=0)
    habilitada = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="img/%y", default="default.svg")
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        txt = "Nombre: {0}, Direccion: {1} {2}, Vacuna: {3}, Canales: {4}, Espera maxima (mins): {5}, User: {6}"
        return txt.format(self.nombre, self.calle, self.numero, self.vacuna, self.canales, self.espera_maxima, self.User)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Sede.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.sede.save()

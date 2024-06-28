from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import datetime

class Organizacion(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, unique=True)
    descripcion = models.CharField(max_length=250,)
    direccion = models.CharField(max_length=250,)
    telefono = models.CharField(max_length=20,)

    en_supervision = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Organización"
        verbose_name_plural = "Organizaciones"

class Reporte(models.Model):

    ingresos_anuales = models.IntegerField()
    gastos_de_capital = models.IntegerField()
    proyectos = models.IntegerField()
    deudas_actuales = models.IntegerField()
    personal = models.IntegerField()
    costos_de_personal = models.IntegerField()
    fecha = models.DateField(auto_now=True)

    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

from django.db import models
from django.utils.timezone import now
from user.models import Userperfil

class Organizacion(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, unique=True)
    descripcion = models.CharField(max_length=250,)
    direccion = models.CharField(max_length=250,)
    telefono = models.CharField(max_length=20,)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Organizacion"
        verbose_name_plural = "Organizaciones"

class Reporte(models.Model):

    ingresos_anuales = models.IntegerField()
    costos_fijos = models.IntegerField()
    costos_variables = models.IntegerField()
    gastos_de_capital = models.IntegerField()
    metas_corto_largo_plazo = models.CharField(max_length=50)
    proyectos = models.IntegerField()
    condiciones_económicas = models.CharField(max_length=50)
    deudas_actuales = models.IntegerField()
    personal = models.IntegerField()
    costos_de_ersonal = models.IntegerField()
    necesidades_tecnológicas = models.CharField(max_length=50)
    reservas_de_contingencia = models.IntegerField()

    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

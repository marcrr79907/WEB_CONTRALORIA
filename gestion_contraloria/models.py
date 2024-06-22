from django.db import models
from django.utils.timezone import now
from user.models import Userperfil

class Organizacion(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, unique=True)
    descripcion = models.CharField(max_length=250,)
    direccion = models.CharField(max_length=250,)
    telefono = models.CharField(max_length=20,)
    

class Reporte(models.Model):

    

    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.PROTECT)

class Presupuesto(models.Model):
    
    fecha = models.DateField(auto_now=True)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.CharField(max_length=20)

    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.PROTECT)
    user_id = models.ForeignKey(Userperfil, on_delete=models.PROTECT)
    reporte_id = models.ForeignKey(Reporte, on_delete=models.PROTECT)

# class Transaccion(models.Model):
    
#     fecha_transaccion = models.DateTimeField(auto_now_add=True)
#     monto = models.DecimalField(max_digits=15, decimal_places=2)
#     descripcion = models.CharField(max_length=250,)

#     id_presupuesto = models.ForeignKey(Presupuesto, on_delete=models.PROTECT)

##################################################################################

    
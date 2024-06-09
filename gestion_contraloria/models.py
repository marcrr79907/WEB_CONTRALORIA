from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Organizacion(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, unique=True)
    descripcion = models.CharField(max_length=250,)
    direccion = models.CharField(max_length=250,)
    telefono = models.CharField(max_length=20,)
    

class Presupuesto(models.Model):
    
    año = models.IntegerField(null=False)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.CharField(max_length=20)

    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.SET_NULL)

class Transaccion(models.Model):
    
    fecha_transaccion = models.DateTimeField(auto_now_add=True, default=datetime.now)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.CharField(max_length=250,)

    id_presupuesto = models.ForeignKey(Presupuesto, on_delete=models.SET_NULL)

class Auditoria(models.Model):
    
    fecha_inicio = models.DateTimeField(auto_now_add=True, default=datetime.now)
    fecha_fin = models.DateTimeField(auto_now_add=True, default=datetime.now)
    estado = models.CharField(max_length=20)

    organizacion_id = models.ForeignKey(Organizacion, on_delete=models.SET_NULL)
    id_auditor = models.ForeignKey(User, on_delete=models.SET_NULL)

class Hallazgo (models.Model):
    
    descripcion = models.CharField(max_length=250,)
    recomendacion = models.CharField(max_length=250,)
    estado = models.CharField(max_length=20)

    id_auditoria = models.ForeignKey(Auditoria, on_delete=models.SET_NULL)

class InformesFinancieros(models.Model):
    pass
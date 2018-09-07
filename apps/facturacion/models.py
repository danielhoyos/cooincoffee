from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cooperativa(models.Model):
    nit         = models.CharField(max_length = 15)
    nombre      = models.CharField(max_length = 50)
    ciudad      = models.CharField(max_length = 20)
    direccion   = models.CharField(max_length = 100)
    telefono    = models.CharField(max_length = 15)
    estado      = models.BooleanField(default = True)

class Asociado(models.Model):
    documento   = models.CharField(max_length = 15)
    nombre      = models.CharField(max_length = 30)
    apellido    = models.CharField(max_length = 30)
    direccion   = models.CharField(max_length = 100, null = True, blank = True)
    telefono    = models.CharField(max_length = 15, null = True, blank = True)
    estado      = models.BooleanField(default = True)

class TipoCafe(models.Model):
    nombre = models.CharField(max_length = 50)

class Factura(models.Model):
    fechaRegistro = models.DateTimeField()
    cooperativa   = models.ForeignKey(Cooperativa, on_delete = models.PROTECT)
    usuario       = models.ForeignKey(User, on_delete = models.PROTECT)

class DetalleFactura(models.Model):
    cantidad    = models.IntegerField()
    unidad      = models.CharField(max_length = 20, default = 'Kilo')
    valorTotal  = models.IntegerField()
    idTipoCafe  = models.ForeignKey(TipoCafe, on_delete = models.PROTECT)
    idAsociado  = models.ForeignKey(Asociado, on_delete = models.PROTECT)
    idFactura   = models.ForeignKey(Factura, on_delete = models.PROTECT)
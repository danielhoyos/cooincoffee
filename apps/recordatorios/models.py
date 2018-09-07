from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recordatorio(models.Model):
    nombre      = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100, null = True, blank = True)
    fecha       = models.DateField()
    estado      = models.BooleanField(default = False)
    usuario     = models.ManyToManyField(User)
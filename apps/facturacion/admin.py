from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cooperativa)
admin.site.register(Asociado)
admin.site.register(TipoCafe)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
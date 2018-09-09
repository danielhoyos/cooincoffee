from django.urls import path, include
from .views import *

urlpatterns = [
    path('', facturacion_view, name = "facturacion"),
    path('cooperativas/', cooperativas_view, name = "cooperativas"),
    path('asociados/', asociados_view, name = "asociados"),
    path('tipos_cafe/', tipos_cafe_view, name = "tipos_cafe"),
    path('reportes/', reportes_view, name = "reportes"),
]
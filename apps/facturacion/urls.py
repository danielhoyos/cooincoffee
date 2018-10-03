from django.urls import path, include
from .views import *

urlpatterns = [
    path('', facturacion_view, name = "facturacion"),
    path('facturacion/codigo/', facturacion_codigo_view, name = "facturacion_codigo"),
    
    path('cooperativas/', cooperativas_view, name = "cooperativas"),
    path('cooperativas/<int:id_cooperativa>/', cooperativa_editar_view, name = "cooperativa_editar"),

    path('asociados/', asociados_view, name = "asociados"),
    path('asociados/<int:id_asociado>/', asociado_editar_view, name = "asociado_editar"),

    path('tipos_cafe/', tipos_cafe_view, name = "tipos_cafe"),
    path('tipos_cafe/<int:id_tipo_cafe>/', tipo_cafe_editar_view, name = "tipo_cafe_editar"),
    path('tipos_cafe/eliminar/<int:id_tipo_cafe>/', tipo_cafe_eliminar_view, name = "tipo_cafe_eliminar"),
    
    path('ventas/', ventas_view, name = "ventas"),
    path('ventas/<int:id_factura>/', ventas_ver_view, name = "ventas_ver"),

    path('reportes/', reportes_view, name = "reportes"),
    path('reporte_data/', reporte_data, name = "reporte_data"),
    path('reporte_cooperativas/', reporte_cooperativas, name = "reporte_cooperativas"),
    path('reporte_kilos/', reporte_kilos, name = "reporte_kilos"),
    path('reporte_tipos/', reporte_tipos, name = "reporte_tipos"),
]
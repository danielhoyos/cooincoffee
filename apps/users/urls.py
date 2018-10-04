from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('perfil/', perfil_view, name = "perfil"),
    path('change_password/', change_password_view, name = "change_password"),
    path('usuarios/', usuarios_view, name = "usuarios"),
    path('usuarios/<int:id_usuario>/', usuario_editar_view, name = "usuario_editar"),
    path('', include("apps.facturacion.urls")),
    path('recordatorios/', include("apps.recordatorios.urls")),
]
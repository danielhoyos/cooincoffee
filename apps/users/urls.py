from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('perfil/', perfil_view, name = "perfil"),
    path('', include("apps.facturacion.urls")),
    path('recordatorios/', include("apps.recordatorios.urls")),
]
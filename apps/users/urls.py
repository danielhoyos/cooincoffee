from django.urls import path
from .views import *
from apps.facturacion.views import *
from apps.recordatorios.views import *

urlpatterns = [
    path('', recordatorios_view, name = "recordatorios"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
]
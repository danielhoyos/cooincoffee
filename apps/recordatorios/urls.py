from django.urls import path
from .views import *

urlpatterns = [
    path('', recordatorios_view, name = "recordatorios"),
]
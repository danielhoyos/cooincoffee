from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/system/login/')
def facturacion_view(request):
    return render(request, 'facturacion/index.html', locals())

@login_required(login_url = '/system/login/')
def cooperativas_view(request):
    return render(request, 'facturacion/cooperativas.html', locals())

@login_required(login_url = '/system/login/')
def asociados_view(request):
    return render(request, 'facturacion/asociados.html', locals())

@login_required(login_url = '/system/login/')
def tipos_cafe_view(request):
    return render(request, 'facturacion/tipos_cafe.html', locals())

@login_required(login_url = '/system/login/')
def reportes_view(request):
    return render(request, 'facturacion/reportes.html', locals())
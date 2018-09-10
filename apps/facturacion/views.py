from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

from .models import *
from .forms import *

# Facturación
@login_required(login_url = '/system/login/')
def facturacion_view(request):
    detalle_factura_formset = formset_factory(detalle_factura_form, max_num=10)

    if request.user.is_superuser:
        if request.method == 'POST':
            form_factura = factura_form(request.POST)
            form_detalle_factura = detalle_factura_formset(request.POST)

            if form_factura.is_valid() and form_detalle_factura.is_valid():
                # Factura
                factura = form_factura.save(commit = False)
                factura.usuario = request.user
                factura.save()

                # Detalle Factura
                for detalle in form_detalle_factura.forms:
                    detalle_factura = detalle.save(commit = False)
                    detalle_factura.idFactura = factura
                    detalle_factura.save()
            
                return redirect('facturacion')
        else:
            form_factura         = factura_form()
            form_detalle_factura = detalle_factura_formset()
    else:
        return redirect('reportes')
    
    return render(request, 'facturacion/index.html', locals())

@login_required(login_url = '/system/login/')
def facturacion_codigo_view(request):
    factura = Factura.objects.filter(codigo = request.GET['codigo'])
    data = serializers.serialize('json', factura)

    return HttpResponse(data, content_type = 'application/json')
# Fin Facturación

# Cooperativa
@login_required(login_url = '/system/login/')
def cooperativas_view(request):
    if request.method == 'POST':
        form_agregar_cooperativa = agregar_cooperativa_form(request.POST)
        if form_agregar_cooperativa.is_valid():
            form_agregar_cooperativa.save()
            return redirect('cooperativas')
    else:
        form_agregar_cooperativa = agregar_cooperativa_form()

    lista_cooperativas = Cooperativa.objects.all()

    return render(request, 'facturacion/cooperativas.html', locals())

@login_required(login_url = '/system/login/')
def cooperativa_editar_view(request, id_cooperativa):
    if request.user.is_superuser:
        cooperativa = Cooperativa.objects.get(id = id_cooperativa)

        if request.method == 'POST':
            form_editar_cooperativa = agregar_cooperativa_form(request.POST, request.FILES, instance = cooperativa)
            if form_editar_cooperativa.is_valid():
                form_editar_cooperativa.save()
                return redirect('cooperativa_editar', id_cooperativa = id_cooperativa)
        else:
            form_editar_cooperativa = agregar_cooperativa_form(instance = cooperativa)   

        return render(request, 'facturacion/cooperativas_editar.html', locals())
    else:
        return redirect('cooperativas')
# Fin Cooperativas

# Asociados
@login_required(login_url = '/system/login/')
def asociados_view(request):
    if request.method == 'POST':
        form_agregar_asociado = agregar_asociado_form(request.POST)
        if form_agregar_asociado.is_valid():
            form_agregar_asociado.save()
            return redirect('/system/asociados/')
    else:
        form_agregar_asociado = agregar_asociado_form()

    lista_asociados = Asociado.objects.all()

    return render(request, 'facturacion/asociados.html', locals())

@login_required(login_url = '/system/login/')
def asociado_editar_view(request, id_asociado):
    asociado = Asociado.objects.get(id = id_asociado)

    if request.method == 'POST':
        form_editar_asociado = agregar_asociado_form(request.POST, request.FILES, instance = asociado)
        if form_editar_asociado.is_valid():
            form_editar_asociado.save()
            return redirect('asociado_editar', id_asociado = id_asociado)
    else:
        form_editar_asociado = agregar_asociado_form(instance = asociado)   

    return render(request, 'facturacion/asociados_editar.html', locals())
# Fin Asociados

# Tipos Café
@login_required(login_url = '/system/login/')
def tipos_cafe_view(request):
    if request.method == 'POST':
        form_agregar_tipo_cafe = agregar_tipo_cafe_form(request.POST)
        if form_agregar_tipo_cafe.is_valid():
            form_agregar_tipo_cafe.save()
            return redirect('/system/tipos_cafe/')
    else:
        form_agregar_tipo_cafe = agregar_tipo_cafe_form()

    lista_tipos_cafe = TipoCafe.objects.all()

    return render(request, 'facturacion/tipos_cafe.html', locals())

@login_required(login_url = '/system/login/')
def tipo_cafe_editar_view(request, id_tipo_cafe):
    tipo_cafe = TipoCafe.objects.get(id = id_tipo_cafe)

    if request.method == 'POST':
        form_editar_tipo_cafe = agregar_tipo_cafe_form(request.POST, request.FILES, instance = tipo_cafe)
        if form_editar_tipo_cafe.is_valid():
            form_editar_tipo_cafe.save()
            return redirect('tipo_cafe_editar', id_tipo_cafe = id_tipo_cafe)
    else:
        form_editar_tipo_cafe = agregar_tipo_cafe_form(instance = tipo_cafe)   

    return render(request, 'facturacion/tipos_cafe_editar.html', locals())

@login_required(login_url = '/system/login/')
def tipo_cafe_eliminar_view(request, id_tipo_cafe):
    tipo_cafe = TipoCafe.objects.get(id = id_tipo_cafe)
    tipo_cafe.delete()

    return redirect('/system/tipos_cafe/')
# Fin Tipos Café

@login_required(login_url = '/system/login/')
def reportes_view(request):
    return render(request, 'facturacion/reportes.html', locals())
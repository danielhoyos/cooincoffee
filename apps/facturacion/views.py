from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from django.db.models.functions import ExtractYear
import datetime
import json

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
                    detalle_factura.factura = factura
                    detalle_factura.save()
            
                return redirect('ventas_ver', id_factura = factura.id)
        else:
            form_factura         = factura_form()
            form_detalle_factura = detalle_factura_formset()
    else:
        return redirect('ventas')
    
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

# Ventas
@login_required(login_url = '/system/login/')
def ventas_view(request):
    lista_facturas = Factura.objects.all()

    return render(request, 'facturacion/ventas.html', locals())

@login_required(login_url = '/system/login/')
def ventas_ver_view(request, id_factura):
    factura = Factura.objects.get(id = id_factura)
    detalles_factura = DetalleFactura.objects.filter(factura = id_factura)
    total = 0

    for detalle_factura in detalles_factura:
        total += detalle_factura.total

    return render(request, 'facturacion/ventas_ver.html', locals())
# Fin Ventas

# Reportes
@login_required(login_url = '/system/login/')
def reportes_view(request):
    cooperativas = Cooperativa.objects.all();
    asociados = Asociado.objects.all();
    years = Factura.objects.values_list(ExtractYear('fecha_registro'), flat = True).distinct()

    date = datetime.date.today();
    year_now = date.year
    return render(request, 'facturacion/reportes.html', locals())

@login_required(login_url = '/system/login/')
def reporte_data(request):
    # Valores por defecto
    months = {
        1 : "Enero",
        2 : "Febrero",
        3 : "Marzo",
        4 : "Abril",
        5 : "Mayo",
        6 : "Junio",
        7 : "Julio",
        8 : "Agosto",
        9 : "Septiembre",
        10 : "Octubre",
        11 : "Noviembre",
        12 : "Diciembre",
    }
    data_report = {
        'labels' : [],
        'label' : [],
        'data' : [],
        'total' : 0   
    }

    # Valores para filtrar
    coop = request.GET.get('cooperativa')
    asoc = request.GET.get('asociado')
    year = request.GET.get('year', 2018)

    data_report['title'] = "Reporte mensual del Año " + str(year)

    if coop != None:
        cooperativa = Cooperativa.objects.get(pk = coop)
        data_report['title'] += ' | Cooperativa: ' + str(cooperativa.nombre)

    if asoc != None:
        asociado = Asociado.objects.get(pk = asoc)
        data_report['title'] += ' | Asociado: ' + str(asociado.nombre) + ' ' + str(asociado.apellido)

    # Consultas
    for month in range(1, 13):
        total = DetalleFactura.objects.select_related('factura').filter(factura__fecha_registro__month = month, factura__fecha_registro__year = year)

        if asoc != None:
            total = total.filter(asociado = asoc)

        if coop != None:
            total = total.filter(factura__cooperativa = coop)

        total = total.aggregate(Sum('total'))

        data_report['labels'].append(months[month])
        data_report['data'].append(total['total__sum'])

        if(total['total__sum']):
            data_report['total'] += total['total__sum']
    
    # Obteniendo la consulta y creando respuesta
    return JsonResponse(data_report)

def reporte_cooperativas(request):
     # Valores por defecto
    cooperativas = Cooperativa.objects.all();
    data_cooperativas = []

    # Valores para filtrar
    year = request.GET.get('year', 2018)

    data_report = {
        'total' : 0,
        'year' : year
    }

    # Consultas
    for cooperativa in cooperativas:
        total = DetalleFactura.objects.select_related('factura').filter(factura__cooperativa = cooperativa.id, factura__fecha_registro__year = year).aggregate(Sum('total'))
        cooperativa_data = {
            'cooperativa':cooperativa.nombre,
            'total':total['total__sum']
        }
        data_cooperativas.append(cooperativa_data)
        if(total['total__sum']):
            data_report['total'] += total['total__sum']

    data_report['cooperativas'] = data_cooperativas
    return JsonResponse(data_report)

def reporte_kilos(request):
     # Valores por defecto
    tipos_cafe = TipoCafe.objects.all()
    data_kilos = []

    # Valores para filtrar
    year = request.GET.get('year', 2018)

    data_report = {
        'total' : 0,
        'year' : year
    }

    # Consultas
    for tipo_cafe in tipos_cafe:
        total = DetalleFactura.objects.select_related('factura').filter(tipo_cafe = tipo_cafe.id, factura__fecha_registro__year = year).aggregate(Sum('cantidad'))
        kilo_data = {
            'tipo_cafe':tipo_cafe.nombre,
            'total': total['cantidad__sum'] if total['cantidad__sum'] != None  else 0
        }
        data_kilos.append(kilo_data)
        if(total['cantidad__sum']):
            data_report['total'] += total['cantidad__sum']

    data_report['kilos'] = data_kilos
    return JsonResponse(data_report)

def reporte_tipos(request):
     # Valores por defecto
    tipos_cafe = TipoCafe.objects.all()
    data_ventas = []

    # Valores para filtrar
    year = request.GET.get('year', 2018)

    data_report = {
        'total' : 0,
        'year' : year
    }

    # Consultas
    for tipo_cafe in tipos_cafe:
        total = DetalleFactura.objects.select_related('factura').filter(tipo_cafe = tipo_cafe.id, factura__fecha_registro__year = year).aggregate(Sum('total'))
        tipo_data = {
            'tipo_cafe':tipo_cafe.nombre,
            'total': total['total__sum'] if total['total__sum'] != None  else 0
        }
        data_ventas.append(tipo_data)
        if(total['total__sum']):
            data_report['total'] += total['total__sum']

    data_report['ventas'] = data_ventas
    return JsonResponse(data_report)
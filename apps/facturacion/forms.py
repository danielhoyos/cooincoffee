from django import forms
from .models import *

class agregar_cooperativa_form(forms.ModelForm):
    class Meta: 
        model   = Cooperativa
        fields  = '__all__'
        widgets = {
            'nit'       : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'nombre'    : forms.TextInput(attrs = { 'class' : 'form-control' }),  
            'ciudad'    : forms.TextInput(attrs = { 'class' : 'form-control' }), 
            'direccion' : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'telefono'  : forms.NumberInput(attrs = { 'class' : 'form-control' }), 
            'logo'      : forms.FileInput(attrs = { 'class' : 'form-control-file' }),
            'estado'    : forms.CheckboxInput(attrs = { 'class' : 'form-check-input' }),
        }

class agregar_asociado_form(forms.ModelForm):
    class Meta: 
        model   = Asociado
        fields  = '__all__'
        widgets = {
            'documento' : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'nombre'    : forms.TextInput(attrs = { 'class' : 'form-control' }),  
            'apellido'  : forms.TextInput(attrs = { 'class' : 'form-control' }), 
            'direccion' : forms.TextInput(attrs = { 'class' : 'form-control' }),
            'telefono'  : forms.NumberInput(attrs = { 'class' : 'form-control' }), 
            'estado'    : forms.CheckboxInput(attrs = { 'class' : 'form-check-input' }),
        }
        labels = {
            'documento' : 'C.C',
            'direccion' : 'Dirección'
        }

class agregar_tipo_cafe_form(forms.ModelForm):
    class Meta: 
        model   = TipoCafe
        fields  = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs = { 'class' : 'form-control' }),
        }

class factura_form(forms.ModelForm):
    class Meta: 
        model   = Factura
        fields  = ('codigo', 'cooperativa', 'fechaRegistro')
        widgets = {
            'codigo' : forms.TextInput(attrs = { 'class' : 'text-center', 'size' : '10', 'placeholder' : 'A1-000', 'id' : 'codigo-factura'}),
            'cooperativa' : forms.Select(attrs = { 'class' : 'form-control' }),
            'fechaRegistro' : forms.TextInput(attrs = { 'class' : 'form-control', 'type' : 'date'})
        }
        labels = {
            'fechaRegistro' : 'Fecha'
        }

class detalle_factura_form(forms.ModelForm):
    class Meta:
        model   = DetalleFactura
        fields  = '__all__'
        exclude = ['idFactura']
        widgets = {
            'cantidad'  : forms.NumberInput(attrs = { 'class' : 'form-control' }),
            'unidad'    : forms.TextInput(attrs = { 'class' : 'form-control', 'readonly' : 'true'}),
            'total': forms.NumberInput(attrs = { 'class' : 'form-control' }),
            'idTipoCafe': forms.Select(attrs = { 'class' : 'form-control' }),
            'idAsociado': forms.Select(attrs = { 'class' : 'form-control' })        
        }

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

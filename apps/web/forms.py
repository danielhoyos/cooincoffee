from django import forms

class contacto_form(forms.Form):
    nombre  = forms.CharField(label = False, widget = forms.TextInput(attrs = { 'class' : 'form-control mb-3' , 'placeholder': 'Nombre'}))
    email   = forms.EmailField(label = False, widget = forms.TextInput(attrs = { 'class' : 'form-control mb-3' , 'placeholder': 'E-mail'}))
    mensaje = forms.CharField(label = False, widget = forms.Textarea(attrs = { 'class' : 'form-control mb-3' , 'placeholder': 'Mensaje'}))
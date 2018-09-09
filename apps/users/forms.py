from django import forms

class login_form(forms.Form):
    usuario = forms.CharField(label = False, widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Usuario' }))
    password = forms.CharField(label = False, widget = forms.PasswordInput(render_value = False, attrs={'class' : 'form-control', 'placeholder' : 'Contraseña' }))
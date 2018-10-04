from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

class login_form(forms.Form):
    usuario = forms.CharField(label = False, widget = forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Usuario' }))
    password = forms.CharField(label = False, widget = forms.PasswordInput(render_value = False, attrs={'class' : 'form-control', 'placeholder' : 'Contraseña' }))

class profile_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        widgets = {
            'first_name' : forms.TextInput(attrs = { 'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs = { 'class' : 'form-control'}),
            'username' : forms.TextInput(attrs = { 'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs = { 'class' : 'form-control'})
        }
        labels = {
            'first_name' : 'Nombres',
            'last_name' : 'Apellidos',
            'username' : 'Usuario',
            'email' : 'E-mail'
        }

class change_password_form(forms.Form):
    passwordold = forms.CharField(label = "Actual", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))
    passwordnew1 = forms.CharField(label = "Nueva", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))
    passwordnew2 = forms.CharField(label = "Confirmar", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))

    def clean_passwordnew2(self):
        passwordnew1 = self.cleaned_data['passwordnew1']
        passwordnew2 = self.cleaned_data['passwordnew2']

        if passwordnew1 == passwordnew2:
            pass
        else:
            raise forms.ValidationError('Los contraseñas con coinciden')
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

class agregar_usuario_form(forms.Form):
    CHOISES = (('jefe', 'Jefe'), ('secretaria', 'Secretaria'), ('contador', 'Contador (a)'))

    first_name  = forms.CharField(label = "Nombre",widget = forms.TextInput(attrs={ 'class' : 'form-control' }))
    last_name   = forms.CharField(label = "Apellido",widget = forms.TextInput(attrs={ 'class' : 'form-control' }))
    username    = forms.CharField(label = "Usuario",widget = forms.TextInput(attrs={ 'class' : 'form-control' }))
    email       = forms.EmailField(label = "E-mail",widget = forms.TextInput(attrs={ 'class' : 'form-control' }))
    password1   = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))
    password2   = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))
    rol         = forms.ChoiceField(label = "Rol", widget = forms.Select(attrs={ 'class' : 'form-control' }), choices=CHOISES)

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            u = User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de Usuario ya registrado')

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            e = User.objects.get(email = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Correo Electronico ya registrado')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 == password2:
            pass
        else:
            raise forms.ValidationError('Los password con coinciden')

class update_usuario_form(forms.Form):
    CHOISES_ROL = (('jefe', 'Jefe'), ('secretaria', 'Secretaria'), ('contador', 'Contador (a)'))
    CHOISES_ESTADO = ((1, 'Activo (a)'), (0, 'Inactivo (a)'))
    
    estado = forms.ChoiceField(label = "Estado", widget = forms.Select(attrs={ 'class' : 'form-control' }), choices=CHOISES_ESTADO)
    rol    = forms.ChoiceField(label = "Rol", widget = forms.Select(attrs={ 'class' : 'form-control' }), choices=CHOISES_ROL)    
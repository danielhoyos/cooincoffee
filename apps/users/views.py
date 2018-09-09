from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/system/')
    else:
        if request.method == 'POST':
            formulario = login_form(request.POST)
            if formulario.is_valid():
                usuario_form = formulario.cleaned_data['usuario']
                password_form = formulario.cleaned_data['password']

                usuario = authenticate(username = usuario_form, password = password_form)

                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return redirect('/system/')
                else:
                    msg = 'El usuario o la contraseña son incorrectos.'
        else:
            formulario = login_form()

    return render(request, 'users/login.html', locals())

@login_required(login_url = '/system/login/')
def perfil_view(request):
    return render(request, 'users/perfil.html', locals())

@login_required(login_url = '/system/login/')
def logout_view(request):
    logout(request)
    return redirect('/system/')
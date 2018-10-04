from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

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
    if request.method == 'POST':
        formulario = profile_form(request.POST, instance = request.user)
        
        if formulario.is_valid():
            formulario.save()
    
    else:
        formulario = profile_form(instance = request.user)

    return render(request, 'users/perfil.html', locals())

@login_required(login_url = '/system/login/')
def change_password_view(request):
    if request.method == 'POST':
        formulario_password = change_password_form(request.POST)   

        if formulario_password.is_valid():
            passwordold = formulario_password.cleaned_data['passwordold']
            passwordnew1 = formulario_password.cleaned_data['passwordnew1']
            passwordnew2 = formulario_password.cleaned_data['passwordnew2']

            if request.user.check_password(passwordold):
                usuario = User.objects.get(username = request.user)
                usuario.set_password(passwordnew1)
                usuario.save()
                update_session_auth_hash(request, usuario)
                return redirect('/system/perfil/')
    else:
        formulario_password = change_password_form()
    
    return render(request, 'users/change_password.html', locals())

@login_required(login_url = '/system/login/')
def logout_view(request):
    logout(request)
    return redirect('/system/')
from django.shortcuts import render
from .forms import contacto_form

# Create your views here.
def index_view(request): 
    info_enviada = False
    nombre  = ''
    email   = ''
    mensaje = ''

    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            info_enviada = True
            nombre  = formulario.cleaned_data['nombre']
            email   = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['mensaje']
        
    else:
        formulario = contacto_form()

    return render(request, 'web/index.html', locals())
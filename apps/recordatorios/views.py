from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/system/login/')
def recordatorios_view(request):
    return render(request, 'recordatorios/index.html', locals())
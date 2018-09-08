from apps.facturacion.models import TipoCafe, Cooperativa

def tiposCafe(request):
    listTiposCafe = TipoCafe.objects.all()
    context = { 'listTiposCafe' : listTiposCafe }

    return context

def cooperativas(request):
    listCooperativas = Cooperativa.objects.all()
    context = {'listCooperativas' : listCooperativas}

    return context
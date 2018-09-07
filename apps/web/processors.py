from apps.facturacion.models import TipoCafe

def tiposCafe(request):
    listTiposCafe = TipoCafe.objects.all()
    context = {}
    lista = []

    for tipoCafe in listTiposCafe:
        lista.append(tipoCafe.nombre)

    context['tiposCafe'] = lista
    return context
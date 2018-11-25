from django.shortcuts import render
from .models import Almoxarifado

def list_itens(request):
    itens = Almoxarifado.objects.all()
    return render(request, 'lista.html', {'itens': itens})

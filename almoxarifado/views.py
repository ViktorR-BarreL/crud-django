from django.shortcuts import render, redirect
from .models import Almoxarifado
from .forms import AlmoxarifadoForm

def list_itens(request):
    itens = Almoxarifado.objects.all()
    return render(request, 'lista.html', {'itens': itens})

def create_itens(request):
    form = AlmoxarifadoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_itens')

    return render(request, 'form.html', {'form':form})
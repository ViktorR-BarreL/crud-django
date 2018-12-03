from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def list_itens(request):
    itens = Item.objects.all()
    return render(request, 'lista.html', {'itens': itens})

def create_itens(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_itens')

    return render(request, 'form.html', {'form':form})

def update_itens(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('list_itens')

    return render(request, 'form.html', {'form': form,})

def delete_itens(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('list_itens')

    return render(request, 'delete.html', {'item': item})

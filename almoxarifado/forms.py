from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'descrição', 'quantidade', 'usuário', 'categoria']
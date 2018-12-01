from django import forms
from .models import Almoxarifado

class AlmoxarifadoForm(forms.ModelForm):
    class Meta:
        model = Almoxarifado
        fields = ['nome', 'descrição', 'quantidade', 'usuário']
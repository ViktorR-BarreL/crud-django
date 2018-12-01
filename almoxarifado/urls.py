from django.urls import path
from .views import list_itens, create_itens

urlpatterns = [
    path('', list_itens, name="list_itens"),
    path('cadastro', create_itens, name="create_itens")
]
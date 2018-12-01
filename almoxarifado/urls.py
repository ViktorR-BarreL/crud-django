from django.urls import path
from .views import list_itens, create_itens, update_itens, delete_itens

urlpatterns = [
    path('', list_itens, name="list_itens"),
    path('cadastro', create_itens, name="create_itens"),
    path('edicao/<int:id>', update_itens, name="update_itens"),
    path('remocao/<int:id>', delete_itens, name="delete_itens")
]
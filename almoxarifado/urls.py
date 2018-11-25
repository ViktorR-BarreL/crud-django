from django.urls import path
from .views import list_itens

urlpatterns = [
    path('', list_itens, name="list_itens"),
]
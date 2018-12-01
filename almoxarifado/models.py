from django.db import models

class Almoxarifado(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    quantidade = models.PositiveIntegerField()
    usuário = models.CharField(max_length=100)
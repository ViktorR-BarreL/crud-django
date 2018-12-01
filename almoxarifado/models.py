from django.db import models

class Almoxarifado(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=100)
    descrição = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    usuário = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
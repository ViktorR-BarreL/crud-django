from django.db import models

class Item(models.Model):
    id = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    quantidade = models.PositiveIntegerField()
    usuário = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    id = models.IntegerField(primary_key= True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
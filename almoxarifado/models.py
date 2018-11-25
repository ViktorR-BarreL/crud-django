from django.db import models

class Almoxarifado(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
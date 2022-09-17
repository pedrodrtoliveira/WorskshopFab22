from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=16)
    sobrenome = models.CharField(max_length=16)
    idade = models.CharField(max_length=2)
    nascimento = models.DateField()
    descricao = models.TextField(max_length=200)
from ctypes import resize
from gettext import NullTranslations
from pydoc import describe
from django.db import models

# Create your models here.


class Categorias(models.Model):
    nome = models.CharField( max_length=50)
    horario = models.DateTimeField(auto_now_add=True)


class Reclamacoes(models.Model):
    data = models.DateField()
    assunto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria  = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    descricao = models.TextField(null=True, blank=True)
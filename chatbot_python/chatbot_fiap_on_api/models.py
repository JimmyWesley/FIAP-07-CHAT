from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Resposta(models.Model):
    codigo = models.IntegerField()
    valor = models.CharField(max_length=1)
    descricao = models.TextField()
    acao = models.TextField()

class Pergunta(models.Model):
    codigo = models.IntegerField()
    titulo = models.TextField()
    respostas = models.ManyToManyField(Resposta)
    acao_anterior = models.TextField()
    acao_principal = models.TextField()
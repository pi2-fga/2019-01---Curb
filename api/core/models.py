# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=5)
    cpf = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.IntegerField()
    link = models.CharField(max_length=100)
    usuarioAtivo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=5)
    cpf = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome

class Curb(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.IntegerField()
    link = models.CharField(max_length=100)
    usuarioAtivo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)
    status = models.CharField(max_length=5)

class Monitoramento(models.Model):
    curbAtivo = models.ForeignKey(Curb, on_delete=models.CASCADE)
    status = models.CharField(max_length=5)
    tinta = models.IntegerField()
    bateria = models.IntegerField()
    latitude = models.CharField(max_length=20)
    logitude = models.CharField(max_length=20)
    data = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)

class Relatorio(models.Model):
    curbAtivo = models.ForeignKey(Curb, on_delete=models.CASCADE)
    data = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)
    tintaAtual = models.IntegerField()
    bateriaAtual = models.IntegerField()
    consumoTinta = models.IntegerField()
    consumoBateria = models.IntegerField()


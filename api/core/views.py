# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from .models import Usuario, Carrinho, Trajeto, Bateria, Tinta
from .serializer import UsuarioSerializer, CarrinhoSerializer, TrajetoSerializer, BateriaSerializer, TintaSerializer

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class TrajetoViewSet(viewsets.ModelViewSet):
    queryset = Trajeto.objects.all()
    serializer_class = TrajetoSerializer

class BateriaViewSet(viewsets.ModelViewSet):
    queryset = Bateria.objects.all()
    serializer_class = BateriaSerializer

class TintaViewSet(viewsets.ModelViewSet):
    queryset = Tinta.objects.all()
    serializer_class = TintaSerializer
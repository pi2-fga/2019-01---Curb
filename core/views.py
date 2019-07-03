# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from .models import Usuario, Curb, Monitoramento, Relatorio
from .serializer import UsuarioSerializer, CurbSerializer, MonitoramentoSerializer, RelatorioSerializer

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CurbViewSet(viewsets.ModelViewSet):
    queryset = Curb.objects.all()
    serializer_class = CurbSerializer

class MonitoramentoViewSet(viewsets.ModelViewSet):
    queryset = Monitoramento.objects.all()
    serializer_class = MonitoramentoSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
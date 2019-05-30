from rest_framework import serializers
from .models import Usuario, Carrinho

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'status', 'cpf')

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ('id', 'nome', 'codigo', 'link', 'usuarioAtivo')

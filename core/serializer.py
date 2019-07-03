from rest_framework import serializers
from .models import Usuario, Carrinho, Bateria, Tinta, Trajeto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'status', 'cpf')

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ('id', 'nome', 'codigo', 'link', 'usuarioAtivo')

class BateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bateria
        fields = ('id', 'porcentagem')

class TintaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tinta
        fields = ('id', 'porcentagem')

class TrajetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajeto
        fields = ('latitudeInicial', 'longituteInicial', 'latituteFinal', 'longituteFinal')
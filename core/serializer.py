from rest_framework import serializers
from .models import Usuario, Curb, Monitoramento, Relatorio
# from datetime import date

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'status', 'cpf', 'email')

class CurbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curb
        fields = ('id', 'nome', 'codigo', 'link', 'usuarioAtivo', 'status', 'data', 'hora')


# class HoraCurbField(serializers.Field):
#
#     def hora_curb(self, hora):
#         hora = Curb._meta.get_field('hora')
#         return hora

class MonitoramentoSerializer(serializers.ModelSerializer):
    # hora = HoraCurbField(source='*')
    class Meta:
        model = Monitoramento
        fields = ('id', 'curbAtivo', 'tinta', 'bateria', 'latitudeInicial', 
                'logitudeInicial', 'logitudeFinal', 'latitudeFinal', 'hora', 'data', 'status')


# class TintaField(serializers.Field):
#
#     def consumo_bateria(self, consumoTinta):
#         data_atual = date.today()
#         i = 1
#         consumoTinta = 0
#         while (Monitoramento.objects.get(id=i).data == data_atual):
#             consumoTinta = Monitoramento.objects.get(id=i).tinta
#             i = i + 1
#             consumoTinta = 5
#         return consumoTinta
#
#     def to_representation(self, value):
#         consumoTinta = self.consumo_tinta(value)
#         ret = {
#             "consumoTinta": value.consumoTinta,
#         }
#         return ret
#
#     def to_internal_value(self, data):
#         consumoTinta = self.consumo_tinta(data)
#         ret = {
#             "consumoTinta": data["consumoTinta"],
#         }
#
#         return ret
#
#
# class BateriaField(serializers.Field):
#
#     def consumo_bateria(self, consumoBateria):
#         data_atual = date.today()
#         i = 1
#         consumoBateria = 0
#         while (Monitoramento.objects.get(id=i).data == data_atual):
#             consumoBateria = Monitoramento.objects.get(id=i).bateria
#             i = i + 1
#             #consumoBateria = 7
#         return consumoBateria
#
#     def to_representation(self, value):
#
#         consumoBateria = self.consumo_bateria(value)
#
#         ret = {
#             "consumoBateria": value.consumoBateria,
#         }
#         return ret
#
#     def to_internal_value(self, data):
#         consumoBateria = self.consumo_bateria(data)
#
#         ret = {
#             "consumoBateria" : data["consumoBateria"],
#         }
#
#         return ret


class RelatorioSerializer(serializers.ModelSerializer):

    # consumoTinta = TintaField(source='consumoBateria')
    # consumoBateria = BateriaField(source='consumoTinta')

    class Meta:
        model = Relatorio
        fields = ('id', 'curbAtivo', 'data', 'hora', 'tintaAtual', 'bateriaAtual', 'consumoTinta', 'consumoBateria')
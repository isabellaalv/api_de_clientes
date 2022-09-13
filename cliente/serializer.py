from rest_framework import serializers
from cliente.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'ultima_compra', 'endereco', 'foto']


class GetCliente(serializers.ModelSerializer):
    cliente = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = ['cliente']


class ClienteGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = []
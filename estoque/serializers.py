from rest_framework import serializers


class ProdutoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    modelo = serializers.CharField(max_length=100)
    quantidade_estoque = serializers.IntegerField()
    quantidade_vendido = serializers.IntegerField()
    notas_usuario = serializers.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)
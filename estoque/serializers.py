from django.contrib.auth.models import User
from rest_framework import serializers

from estoque.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        exclude = ["disponivel_produto"]


    vendedor = serializers.CharField()

    def validate_vendedor(self, value):
        try:
            vendedor_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("usuario não existe")
        return vendedor_obj

    def validate_quantidade_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade no estoque não pode ser menor que zero")
        return value

    def validate_valor(self, value):
        if value < 0:
            raise serializers.ValidationError("O valor do pruduto não pode ser menor que zero")
        return value

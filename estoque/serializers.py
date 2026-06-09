from rest_framework import serializers
from estoque.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'modelo', 'quantidade_estoque', 'valor', 'notas_usuario', 'produto_disponivel', 'quantidade_vendido']
    
    def validate_quantidade_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade em estoque não pode ser negativa.")
        return value
    
    def validate_valor(self, value):
        if value < 0:
            raise serializers.ValidationError("O valor não pode ser negativo.")
        return value

    def create(self, validated_data):
        produto = Produto.objects.create(
            nome = validated_data['nome'],
            modelo = validated_data['modelo'],
            quantidade_estoque = validated_data['quantidade_estoque'],
            valor = validated_data['valor']
        )
        return produto
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.quantidade_estoque = validated_data.get('quantidade_estoque', instance.quantidade_estoque)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.produto_disponivel = validated_data.get('produto_disponivel', instance.produto_disponivel)
        instance.save()
        return instance
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from estoque.models import Produto
from estoque.serializers import ProdutoSerializer

class ProdutoDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset= Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


    def perform_destroy(self, instance):
        instance.disponivel_produto = False
        instance.save()

    def delete(self, request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProdutosList(
mixins.ListModelMixin, #adicionar mixin de listagem
mixins.CreateModelMixin, #adicionar mixin de criacao
generics.GenericAPIView, #classe generica
):
    queryset= Produto.objects.filter(disponivel_produto=True)
    serializer_class = ProdutoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

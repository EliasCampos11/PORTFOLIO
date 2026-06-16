from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from estoque.models import Produto
from estoque.serializers import ProdutoSerializer

class ProdutoDetail( generics.RetrieveUpdateDestroyAPIView):
    queryset= Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = "id"
    def perform_destroy(self, instance):
        instance.disponivel_produto = False
        instance.save()

class ProdutosList( generics.ListCreateAPIView):
    
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset= Produto.objects.filter(vendedor__username=username, disponivel_produto=True)
        return queryset


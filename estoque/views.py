from django.shortcuts import get_object_or_404
from estoque.models import Produto
from estoque.serializers import ProdutoSerializer
from django.http import JsonResponse
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
#Create your views here.

class ProdutoList(generics.ListCreateAPIView): # /api/produtos/?username=
    serializer_class = ProdutoSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Produto.objects.filter(vendedor__username=username, produto_disponivel=True)
        return queryset

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView): # /api/produtos/<pk>/
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def perform_destroy (self, instance):
        instance.produto_disponivel = False 
        instance.save()
        
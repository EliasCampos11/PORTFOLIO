from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from estoque.models import Produto
from estoque.serializers import ProdutoSerializer

class IsOwnerOrCreateOnly(permissions.BasePermission):
  '''
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        username = request.query_params.get("username", None)
        if request.user.username == username:
            return True
        return False
'''
class IsVendedor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.vendedor == request.user:
            return True
        return False
    


class ProdutoDetail( generics.RetrieveUpdateDestroyAPIView):
    queryset= Produto.objects.all()
    permission_classes = [IsVendedor]
    serializer_class = ProdutoSerializer
    lookup_field = "id"
    def perform_destroy(self, instance):
        instance.disponivel_produto = False
        instance.save()

class ProdutosList( generics.ListCreateAPIView):
    
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Produto.objects.filter(vendedor__username=username, disponivel_produto=True)
        return queryset


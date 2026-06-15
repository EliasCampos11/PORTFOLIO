from django.shortcuts import get_object_or_404
from estoque.models import Produto
from estoque.serializers import ProdutoSerializer
from django.http import JsonResponse
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.views import APIView

#Create your views here.
@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def produto_detail(request, id):
    obj = get_object_or_404(Produto, id=id) 
    if request.method == 'GET':
    # Lógica para obter os detalhes do produto com base no ID
        serializer = ProdutoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == 'PATCH':
        serializer = ProdutoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200) 
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        serializer = ProdutoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data 
            obj.produto_disponivel = False
            obj.save()
        return Response(validated_data, status=204)

class ProdutoList(APIView):
    def get(self, request): 
        qs = Produto.objects.filter(produto_disponivel=True)
        serializer = ProdutoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request): 
        data = request.data
        serializer = ProdutoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
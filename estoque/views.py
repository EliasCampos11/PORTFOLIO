from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework.views import APIView

from estoque.models import Produto
from estoque.serializers import ProdutoSerializer

class ProdutoDetail(APIView ):
     
    def get_obj(self,id):
        return get_object_or_404(Produto, id=id)

    def get(self, request,id):
        obj = self.get_obj(id=id)
        serializer = ProdutoSerializer(obj)
        return JsonResponse(serializer.data)
    def patch(self, request,id):
        obj = self.get_obj(id=id)
        serializer = ProdutoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request,id):
        obj = self.get_obj(id=id)
        obj.disponivel_produto = False
        obj.save()
        return Response(status=204)

class ProdutosList(APIView):
    def get(self, request):
        qs = Produto.objects.filter(disponivel_produto=True)
        serializer = ProdutoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = request.data
        serializer = ProdutoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

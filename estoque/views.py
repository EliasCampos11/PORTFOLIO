from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response  import Response

from estoque.models import Produto
from estoque.serializers import ProdutoSerializer


@api_view(http_method_names=["GET","PATCH", "DELETE"])
def produto_detail(request, id):
    obj = get_object_or_404(Produto, id=id)
    if request.method == "GET":
        serializer = ProdutoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        serializer = ProdutoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        obj.disponivel_produto = False
        obj.save()
        return Response(status=204)


@api_view(http_method_names=["GET","POST"])
def produtos_list(request):
    if request.method == "GET":
        qs = Produto.objects.filter(disponivel_produto=True)
        serializer = ProdutoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = request.data
        serializer = ProdutoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
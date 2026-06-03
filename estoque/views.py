from django.shortcuts import get_object_or_404
from estoque.models import Produto
from estoque.serializers import ProdutoSerializer
from django.http import JsonResponse

#Create your views here.
def produto_detail(request, id):
    # Lógica para obter os detalhes do produto com base no ID
    obj = get_object_or_404(Produto, id=id)
    serializer = ProdutoSerializer(obj)
    return JsonResponse(serializer.data)
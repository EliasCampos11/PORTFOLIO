from django.urls import path
from django.conf.urls import include
from estoque.views import ProdutoList, ProdutoDetail

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('produtos/<int:pk>/', ProdutoDetail.as_view()),
]



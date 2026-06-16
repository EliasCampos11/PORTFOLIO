from django.urls import path
from django.conf.urls import include
from estoque.views import produto_detail, ProdutosList
urlpatterns = [
    path('produtos/', ProdutosList.as_view()),
    path('produto/<int:id>/', produto_detail),
]

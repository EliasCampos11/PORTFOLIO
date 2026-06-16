from django.urls import path
from django.conf.urls import include
from estoque.views import ProdutoDetail, ProdutosList
urlpatterns = [
    path('produtos/', ProdutosList.as_view()),
    path('produto/<int:id>/', ProdutoDetail.as_view()),
]

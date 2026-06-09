from django.urls import path
from django.conf.urls import include
from estoque.views import produto_detail, produto_list

urlpatterns = [
    path('produtos/', produto_list),
    path('produtos/<int:id>/', produto_detail),
]



from django.urls import path
from django.conf.urls import include
from estoque.views import produto_detail, produtos_list
urlpatterns = [
    path('produtos/', produtos_list),
    path('produto/<int:id>/', produto_detail),
]

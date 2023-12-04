from django.urls import path

from products.views import Product_listAPI, Product_detailAPI


urlpatterns = [
    path('', Product_listAPI, name='product_list'),
    path('<int:pk>/', Product_detailAPI, name='product_detail'),
]
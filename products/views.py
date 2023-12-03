from rest_framework.viewsets import ModelViewSet

from products.serializers import ProductSerializer
from products.models import Product
# Create your views here.

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


Product_listAPI = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

Product_detailAPI = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
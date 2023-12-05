from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from products.serializers import ProductSerializer
from products.models import Product
# Create your views here.

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
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
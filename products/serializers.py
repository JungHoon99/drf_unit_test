from rest_framework.serializers import ModelSerializer

from products.models import Product

class ProductSerializer(ModelSerializer):

    class Meta():
        model = Product
        fields='__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')
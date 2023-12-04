from rest_framework.serializers import ModelSerializer, ValidationError

from products.models import Product

class ProductSerializer(ModelSerializer):

    class Meta():
        model = Product
        fields='__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')

    def validate_price(self, value):
        if value < 0:
            raise ValidationError("가격은 음수일 수 없습니다.")
        return value
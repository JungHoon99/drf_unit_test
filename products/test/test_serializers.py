from django.test import TestCase

from products.models import Product
from products.serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        # 테스트를 위한 초기 데이터 설정
        self.product_data = {'name': '테스트 제품', 'price': 10000}
        self.product = Product.objects.create(**self.product_data)

        # serializer 인스턴스 생성
        self.serializer = ProductSerializer(instance=self.product)

    def test_serializer_contains_expected_fields(self):
        # Serializer가 예상한 필드를 포함하고 있는지 확인
        expected_fields = ['id', 'name', 'price', 'date_created', 'date_modified']
        actual_fields = list(self.serializer.data.keys())

        self.assertCountEqual(expected_fields, actual_fields)

    def test_serializer_data_matches_model_data(self):
        # Serializer의 데이터가 모델 데이터와 일치하는지 확인
        self.assertEqual(self.serializer.data['name'], self.product_data['name'])
        self.assertEqual(self.serializer.data['price'], self.product_data['price'])

    def test_serializer_validation(self):
        # 유효하지 않은 데이터로 serializer를 검증하는 예제
        invalid_data = {'name': '', 'price': -10}
        serializer = ProductSerializer(data=invalid_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertIn('price', serializer.errors)
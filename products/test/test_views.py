from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from django.urls import reverse

from products.models import Product


class ProductListAPITestCase(APITestCase):
    def setUp(self):
        self.url=reverse('product_list')

    def test_list_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_product_create_view(self):
        sample_post={'name': 'pants', 'price': 67000} 

        response = self.client.post(self.url, sample_post)

        self.assertEqual(response.status_code, HTTP_201_CREATED)


class productDetailAPITestCase(APITestCase):
    def setUp(self):
        self.product_name = "shirt"
        self.price = 5000
        self.product = Product.objects.create(name=self.product_name, price=self.price)

    def test_retrieve_view(self):
        # 제품을 가져오는 GET 요청 테스트
        response = self.client.get(f'/product/{self.product.id}/')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_name)

    def test_update_view(self):
        # 제품을 업데이트하는 PUT 요청 테스트
        updated_data = {'name': '업데이트된 제품', 'price': 150}
        response = self.client.put(f'/product/{self.product.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)

        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, '업데이트된 제품')
        self.assertEqual(updated_product.price, 150)

    def test_destroy_view(self):
        # 제품을 삭제하는 DELETE 요청 테스트
        response = self.client.delete(f'/product/{self.product.id}/')

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        with self.assertRaises(Product.DoesNotExist):
            deleted_product = Product.objects.get(id=self.product.id)

    def test_price_raise_view(self):
        updated_data = {'name': '업데이트된 제품', 'price': -150}
        response = self.client.put(f'/product/{self.product.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)
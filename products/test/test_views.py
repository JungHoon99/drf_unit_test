from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.urls import reverse

from products.models import Product
from products.views import Product_listAPI


class ProductListAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = Product_listAPI
        self.url=reverse('product_list')

    def test_product_list_view(self):
        request = self.factory.get(self.url)

        response = self.view(request)

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_product_create_view(self):
        sample_post={'name': 'pants', 'price': 67000}

        request = self.factory.post(self.url, sample_post)

        response = self.view(request)

        self.assertEqual(response.status_code, HTTP_201_CREATED)


class productDetailAPITestCase(APITestCase):
    def setUp(self):
        self.product_name = "shirt"
        self.price = 5000
        self.product = Product.objects.create(name=self.product_name, price=self.price)
        self.client = APIClient()

    def test_get(self):
        # 제품을 가져오는 GET 요청 테스트
        response = self.client.get(f'/product/{self.product.id}/')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product_name)

    def test_update(self):
        # 제품을 업데이트하는 PUT 요청 테스트
        updated_data = {'name': '업데이트된 제품', 'price': 150}
        response = self.client.put(f'/product/{self.product.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)

        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, '업데이트된 제품')
        self.assertEqual(updated_product.price, 150)

    def test_delete(self):
        # 제품을 삭제하는 DELETE 요청 테스트
        response = self.client.delete(f'/product/{self.product.id}/')

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        with self.assertRaises(Product.DoesNotExist):
            deleted_product = Product.objects.get(id=self.product.id)
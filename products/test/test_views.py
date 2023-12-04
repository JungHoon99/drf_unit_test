from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from django.urls import reverse

from products.models import Product
from accounts.test.factorys import UserFactory

class ProductListAPITestCase(APITestCase):
    def setUp(self):
        self.url=reverse('product_list')

    def authenticate(self):
        user = UserFactory.build()

        response = self.client.post(reverse('user_create'), {
            'userid': user.userid,
            'password': user.password,
            'password2': user.password,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
        })

        print(response.data)
        # 출력예시
        # {
        #     'userid': 'bridgetwalker505', 
        #     'name': 'school', 
        #     'email': 'nancysherman@example.net', 
        #     'phone': '010-2679-2840'
        # }

        response = self.client.post(reverse('user_login'), {
            'userid': user.userid,
            'password': user.password,
        })

        print(response.data)
        # 출력예시
        # {
        #     'userid': 1, 
        #     'username': 'school', 
        #     'message': '로그인 성공', 
        #     'token': {
        #         'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNzM3ODQwLCJpYXQiOjE3MDE2OTQ2NDAsImp0aSI6ImQzZDUwMDY4N2Q1NjRhM2M5MTU3M2ViZmIwMGI3ZTliIiwidXNlcl9pZCI6MX0.zgYmjgtPgguNKbHiYBsfX-BdNq1gkjiQGPDN2ispyyc', 
        #         'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjEyNjY0MCwiaWF0IjoxNzAxNjk0NjQwLCJqdGkiOiJhNmE4MGRjMTZiMTY0MGZiYWFiYWY3MTFmMzY0YTk5NCIsInVzZXJfaWQiOjF9.rkjZQb5NIMLqGlpeRmH7jDdMgCT4UjgeGHr9SlxU_5I'
        #     }
        # }

    def test_list_view(self):
        self.authenticate()
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
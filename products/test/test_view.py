from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.status import HTTP_200_OK
from django.urls import reverse


from products.views import Product_listAPI



class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = Product_listAPI
        self.url=reverse('product_list')

    def test_product_list_view(self):
        request = self.factory.get(self.url)

        response = self.view(request)

        self.assertEqual(response.status_code, HTTP_200_OK)

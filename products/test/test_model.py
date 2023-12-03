from django.test import TestCase
from products.models import Product

class ModelTestCase(TestCase):
    """ 이 클래스는 bucketlist 모델을 위한 test suite를 정의합니다."""
    def setUp(self):
        """ 테스트 클라이언트와 기타 테스트 변수를 정의합니다."""
        self.product_name = "shirt"
        self.price = 5000
        self.product = Product.objects.create(name=self.product_name, price=self.price)

    def test_model_create_product(self):
        """ bucketlist 모델을 테스트하면 bucketlist이 생성될 수 있습니다."""
        new_product = Product(name=self.product_name+"1", price=self.price)
        old_count = Product.objects.count()
        self.product = new_product.save()
        new_count = Product.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_update_product(self):
        self.product.price = 10000
        defore_modify_datetime = self.product.date_modified
        self.product.save()
        update_product = Product.objects.get(id=self.product.id)
        after_modify_datetime = update_product.date_modified
        self.assertEqual(update_product.price, 10000)
        self.assertNotEqual(defore_modify_datetime, after_modify_datetime)

    def test_model_delete_product(self):
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Product.DoesNotExist):
            deleted_product = Product.objects.get(id=product_id)
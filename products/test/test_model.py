from django.test import TestCase
from products.models import Product

class ModelTestCase(TestCase):
    def setUp(self):
        # 기본적인 변수 선언
        self.product_name = "shirt"
        self.price = 5000
        self.product = Product.objects.create(name=self.product_name, 
                                              price=self.price)

    def test_model_create_product(self):
        # 새로운 제품 데이터 생성후 데이터 베이스에서 추가 확인
        new_product = Product(name=self.product_name+"1", price=self.price)
        old_count = Product.objects.count()
        self.product = new_product.save()
        new_count = Product.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_update_product(self):
        # 제품 수정후 데이터 수정 여부와 수정시간 변화 확인
        self.product.price = 10000
        defore_modify_datetime = self.product.date_modified
        self.product.save()
        update_product = Product.objects.get(id=self.product.id)
        after_modify_datetime = update_product.date_modified
        self.assertEqual(update_product.price, 10000)
        self.assertNotEqual(defore_modify_datetime, after_modify_datetime)

    def test_model_delete_product(self):
        #데이터 삭제 후 데이터 확인
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Product.DoesNotExist):
            deleted_product = Product.objects.get(id=product_id)
from django.test import TestCase

from accounts.models import MyUser
from accounts.test.factorys import UserFactory

class MyUserModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory.build()

    def test_create(self):
        # 새로운 제품 데이터 생성후 데이터 베이스에서 추가 확인
        new_user = MyUser(
            userid=self.user.userid,
            name=self.user.name,
            email=self.user.email,
            phone=self.user.phone,
            password=self.user.password
        )

        old_count = MyUser.objects.count()
        self.product = new_user.save()
        new_count = MyUser.objects.count()

        self.assertNotEqual(old_count, new_count)
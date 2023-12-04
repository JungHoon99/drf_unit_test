from django.test import TestCase

from accounts.models import MyUser
from accounts.test.factorys import UserFactory

class MyUserModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory.create()

    def test_update(self):
        # 제품 수정후 데이터 수정 여부와 수정시간 변화 확인
        self.user.name = "테스터"
        self.user.save()
        update_user = MyUser.objects.get(id=self.user.id)
        self.assertEqual(update_user.name, "테스터")

    def test_delete(self):
        #데이터 삭제 후 데이터 확인
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(MyUser.DoesNotExist):
            deleted_product = MyUser.objects.get(id=user_id)
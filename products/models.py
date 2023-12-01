from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    price = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """사람이 읽을 수 있는 표현으로 모델 인스턴스를 반환합니다."""
        return "{}".format(self.name)
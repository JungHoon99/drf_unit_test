from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, userid, name, email, phone, password=None):

        if not userid:
            raise ValueError('사용자 아이디를 입력해주세요.')

        if not email:
            raise ValueError('이메일을 입력해주세요.')

        if not phone:
            raise ValueError('전화번호를 입력해주세요.')

        user = self.model(
            userid=userid,
            name=name,
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, name, email, phone, password=None):
        user = self.create_user(
            userid=userid,
            password=password,
            name=name,
            email=self.normalize_email(email),
            phone=phone,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    userid = models.CharField(verbose_name='아이디', max_length=25, unique=True)
    name = models.CharField(verbose_name='회사 이름 혹은 이름', max_length=30)
    email = models.EmailField(verbose_name='회사 이메일 혹은 이메일', max_length=50)
    phone = models.CharField(verbose_name='회사 번호 혹은 번호', max_length=13, unique=True)
    is_active = models.BooleanField(verbose_name='로그인 가능', default=True)
    is_superuser = models.BooleanField(verbose_name='최고관리자', default=False)
    is_staff = models.BooleanField(verbose_name='관리자페이지 접근', default=False)
    last_login = models.DateTimeField(verbose_name='로그인 일시', blank=True, null=True)
    created = models.DateTimeField(verbose_name='등록 일시', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='수정 일시', auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'userid'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email', 'phone']

    class Meta:
        verbose_name_plural = '사용자'

    def __str__(self):
        return f'{self.userid} - {self.email}'
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
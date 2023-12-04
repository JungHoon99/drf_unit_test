import factory
from faker import Faker
from faker.providers.phone_number import Provider

from accounts.models import MyUser

class PhoneNumberProvider(Provider):
    """
    A Provider for phone number.
    """

    def kor_phone_number(self):
        return f'010-{self.msisdn()[:4]}-{self.msisdn()[:4]}'

fake = Faker()
fake.add_provider(PhoneNumberProvider)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MyUser
    
    userid = f"{fake.user_name()}{int(fake.random.random()*1000)}"
    name =  fake.word()
    email = fake.email()
    phone = fake.unique.kor_phone_number()
    password = fake.password()

from django.test import TestCase
from users import models


class UserModelTest(TestCase):
    def test_create_user(self):
        models.User.objects.create(
            first_name='Astolfo',
            username='1234567',
            user_type='Diretor',
            password=123
        )
        user = models.User.objects.get(username='1234567')
        self.assertEqual(user.first_name, 'Astolfo')
        self.assertEqual(user.user_type, 'Diretor')

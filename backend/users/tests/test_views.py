from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='123456789',
            first_name='Astolfo',
            password='testpassword123',
            user_type='Diretor'
        )

    def test_index_unauthenticated(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertFalse(response.context['login'])

    def test_index_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue(response.context['login'])
        self.assertEqual(response.context['first_name'], 'Astolfo')
        self.assertEqual(response.context['user_type'], 'Diretor')


class RegistrarViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registrar_get(self):
        response = self.client.get(reverse('registrar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar.html')

    def test_registrar_post_valid(self):
        data = {
            'first_name': 'Astolfo',
            'cpf': '123456789',
            'user_type': 'Diretor',
            'password': 'testpassword123'
        }
        response = self.client.post(reverse('registrar'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('logar'))
        self.assertTrue(User.objects.filter(username='123456789').exists())

    def test_registrar_post_invalid(self):
        User.objects.create_user(
            username='123456789',
            first_name='Astolfo',
            password='testpassword123',
            user_type='Diretor'
        )
        data = {
            'first_name': 'Outro Astolfo',
            'cpf': '123456789',
            'user_type': 'Diretor',
            'password': 'testpassword123'
        }
        response = self.client.post(reverse('registrar'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('registrar'))


class LogarViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='123456789',
            first_name='Astolfo',
            password='testpassword123',
            user_type='Diretor'
        )

    def test_logar_get(self):
        response = self.client.get(reverse('logar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logar.html')

    def test_logar_post_valid(self):
        data = {
            'cpf': '123456789',
            'password': 'testpassword123'
        }
        response = self.client.post(reverse('logar'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_logar_post_invalid(self):
        data = {
            'cpf': '123456789',
            'password': 'senhaerrada'
        }
        response = self.client.post(reverse('logar'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logar.html')


class LogoutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='123456789',
            first_name='Astolfo',
            password='testpassword123',
            user_type='Diretor'
        )

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertFalse(response.context['login'])

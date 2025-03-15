from django.test import TestCase, Client
from django.urls import reverse


class UsersURLTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertFalse(response.context['login'])

    def test_registrar_url(self):
        response = self.client.get(reverse('registrar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar.html')

    def test_logar_url(self):
        response = self.client.get(reverse('logar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logar.html')

    def test_logout_url(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('login', response.context)
        self.assertFalse(response.context['login'])

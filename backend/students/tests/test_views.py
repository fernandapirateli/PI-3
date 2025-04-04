from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from students.models import Student, Group

User = get_user_model()


class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Cria usuário de teste e faz login
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            user_type='admin'  # Adapte conforme seu modelo
        )
        self.client.login(username='testuser', password='testpass123')

        # Cria dados de teste
        self.group = Group.objects.create(group_name="Turma A")
        self.student = Student.objects.create(
            student_ra="12345678901",
            student_name="Aluno Teste",
            student_diet_restriction="Nenhuma",
            student_group=self.group
        )

    def test_registrar_aluno_view_post_valid(self):
        """Testa registro de aluno com dados válidos"""
        data = {
            'student_name': 'Novo Aluno',
            'student_ra': '98765432109',
            'student_diet_restriction': 'Vegetariano',
            'group_name': 'Turma B',
            'option': 'registrar_salvar'
        }
        response = self.client.post(reverse('registrar_aluno'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(student_ra='98765432109').exists())

    # Teste para perfil_aluno
    def test_perfil_aluno_view(self):
        """Testa visualização do perfil do aluno"""
        response = self.client.post(reverse('perfil_aluno'), {
            'student_id': self.student.pk
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/perfil_aluno.html')
        self.assertEqual(response.context['student'], self.student)

    # Teste para gerir_aluno
    def test_gerir_aluno_editar(self):
        """Testa edição de aluno"""
        response = self.client.post(reverse('gerir_aluno'), {
            'option': 'editar',
            'student_id': self.student.pk
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/editar_aluno.html')

    def test_gerir_aluno_excluir(self):
        """Testa exclusão de aluno"""
        response = self.client.post(reverse('gerir_aluno'), {
            'option': 'excluir',
            'student_id': self.student.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())


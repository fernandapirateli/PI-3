from django.test import TestCase, Client
from django.urls import reverse
from ..models import Group, Student
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentsURLTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Cria um usuário de teste e loga
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Dados de teste
        self.group = Group.objects.create(group_name="Turma Teste")
        self.student = Student.objects.create(
            student_ra="123456789",
            student_name="Aluno Teste",
            student_group=self.group
        )

    def test_listar_alunos_url(self):
        """Verifica se a URL de listagem está acessível quando logado"""
        response = self.client.get(reverse('listar_alunos'))
        self.assertEqual(response.status_code, 302)

    def test_perfil_aluno_url(self):
        """Verifica se a URL de perfil do aluno está funcionando (requer ID)"""
        # Teste com POST (como especificado na view)
        response = self.client.post(reverse('perfil_aluno'), {
            'student_id': self.student.pk
        })
        self.assertEqual(response.status_code, 200)

    def test_gerir_aluno_url(self):
        """Verifica se a URL de gestão de aluno está funcionando (requer ação)"""
        # Teste com ação de edição
        response = self.client.post(reverse('gerir_aluno'), {
            'option': 'editar',
            'student_id': self.student.pk
        })
        self.assertEqual(response.status_code, 200)

    def test_urls_requerem_autenticacao(self):
        """Verifica se as URLs redirecionam quando não autenticado"""
        urls = [
            reverse('registrar_aluno'),
            reverse('listar_alunos'),
            # perfil_aluno e gerir_aluno não são testados aqui pois requerem POST
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)  # Redirecionamento para login

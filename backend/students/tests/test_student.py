from django.test import TestCase
from students.models import Student, Group
from django.core.exceptions import ValidationError


class StudentModelTest(TestCase):
    def setUp(self):
        # Cria um grupo de teste para usar nos relacionamentos
        self.group = Group.objects.create(group_name="Turma A")

        # Dados padrão para criar estudantes
        self.student_data = {
            'student_ra': '12345678901234',
            'student_name': 'Fulano de Tal',
            'student_diet_restriction': 'Vegetariano',
            'student_group': self.group
        }

    def test_student_creation(self):
        """Testa a criação básica de um estudante"""
        student = Student.objects.create(**self.student_data)

        self.assertEqual(student.student_ra, '12345678901234')
        self.assertEqual(student.student_name, 'Fulano de Tal')
        self.assertEqual(student.student_diet_restriction, 'Vegetariano')
        self.assertEqual(student.student_group.group_name, 'Turma A')
        self.assertEqual(str(student), 'Fulano de Tal')

    def test_ra_unique_constraint(self):
        """Testa se RA é único"""
        Student.objects.create(**self.student_data)

        # Tentativa de criar estudante com mesmo RA deve falhar
        with self.assertRaises(ValidationError):
            duplicate_student = Student(**self.student_data)
            duplicate_student.full_clean()

    def test_group_relationship(self):
        """Testa o relacionamento com Group"""
        student = Student.objects.create(**self.student_data)

        # Testa acesso direto ao grupo
        self.assertEqual(student.student_group, self.group)

        # Testa acesso reverso (grupo -> estudantes)
        self.assertIn(student, self.group.student_set.all())


class GroupModelTest(TestCase):
    def test_group_creation(self):
        """Testa criação básica de grupo"""
        group = Group.objects.create(group_name="Turma B")

        self.assertEqual(group.group_name, 'Turma B')
        self.assertEqual(str(group), 'Turma B')  # Testa __str__

    def test_group_name_unique(self):
        """Testa unicidade do nome do grupo"""
        Group.objects.create(group_name="Turma C")

        with self.assertRaises(ValidationError):
            duplicate_group = Group(group_name="Turma C")
            duplicate_group.full_clean()

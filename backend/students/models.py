from django.db import models


def metric_field(verbose_name):
    return models.FloatField(
        default=None,
        verbose_name=verbose_name
    )


class Student(models.Model):
    student_ra = models.CharField(max_length=14, unique=True, default='N/A')
    student_name = models.CharField(max_length=150)
    student_diet_restriction = models.TextField(null=True, blank=True, default=None)
    student_group = models.ForeignKey('Group', on_delete=models.CASCADE)
    student_gender = models.CharField(max_length=1, default='N/A')
    student_age = models.IntegerField(default=0)  # em meses (o ideal seria data nascimento)
    student_height = metric_field('Altura (cm)')
    student_weight = models.IntegerField(default=0, verbose_name='Peso (g)')

# ajeitar formulários de cadastro

    def __str__(self):
        return self.student_name


class Group(models.Model):
    group_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.group_name

from django.db import models


class Student(models.Model):
    student_ra = models.CharField(max_length=14, unique=True, default='N/A')
    student_name = models.CharField(max_length=150)
    student_diet_restriction = models.TextField(blank=True)
    student_group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Group(models.Model):
    group_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.group_name

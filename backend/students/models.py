from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=150)
    student_class = models.CharField(max_length=20)
    student_diet_restriction = models.TextField(blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Group(models.Model):
    group_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.group_name

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_type = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.first_name

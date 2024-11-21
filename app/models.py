from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField('username', max_length=40, unique=True)
    email = models.EmailField('email', unique=True, max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Feedback(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    email = models.EmailField('Email', max_length=50)
    text = models.TextField('Text', max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'Feedback from {self.name}'
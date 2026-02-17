from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # делаем email уникальным
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')
    country = models.CharField(max_length=50, blank=True, verbose_name='Страна')

    # Указываем, что для аутентификации используется email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # поле username всё ещё требуется для создания суперпользователя

    def __str__(self):
        return self.email

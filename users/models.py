from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

NULLABLE = {'null': True, 'blank': True}



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    is_active = models.BooleanField(verbose_name='статус активации')
    token = models.CharField(max_length=255, verbose_name='токен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

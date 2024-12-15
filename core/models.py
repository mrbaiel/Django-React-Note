from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    city = models.CharField(verbose_name='Город', max_length=40, blank=True, null=True)
    district = models.CharField(verbose_name='Область', max_length=50, blank=True, null=True)
    address = models.TextField(verbose_name='Адрес пользователя', null=True)
    phone = models.CharField(verbose_name='Номер телефона',max_length=12, blank=True, null=True)

    def __str__(self):
        return self.username
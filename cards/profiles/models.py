from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    first_name = models.CharField(max_length=50, verbose_name = 'Имя')
    last_name = models.CharField(max_length=50, verbose_name = 'Фамилия')
    birthday = models.DateField(auto_now=False, auto_now_add=False, verbose_name = 'Дата рождения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=None, verbose_name = 'Фото', blank=True)
    owner = models.OneToOneField(User, verbose_name="Категория", on_delete=models.PROTECT, null=False) 


class CardPost(models.Model):
    content = models.TextField(blank=True, verbose_name = 'Контент')
    photo = models.ImageField(upload_to='post_photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=None, verbose_name = 'Фото', blank=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name = 'Дата поста')
    card = models.ForeignKey("card", verbose_name="Карта", on_delete=models.PROTECT, null=True)
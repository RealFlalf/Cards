# Generated by Django 3.1.7 on 2021-03-15 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210314_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(blank=True, upload_to='post_photos/%Y/%m/%d/', verbose_name='Фото')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата поста')),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.card', verbose_name='Карта')),
            ],
        ),
    ]

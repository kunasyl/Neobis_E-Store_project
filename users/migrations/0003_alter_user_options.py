# Generated by Django 4.1.7 on 2023-05-11 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-created_at',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_alter_mebel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mebel',
            name='description',
            field=models.TextField(verbose_name='Описание с куфара'),
        ),
        migrations.AlterField(
            model_name='mebel',
            name='parse_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата прихода к нам'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_message', models.CharField(max_length=200, verbose_name='Кратко о пожелании')),
                ('message', models.TextField(verbose_name='Само пожелание или привет для пользователей')),
            ],
        ),
    ]
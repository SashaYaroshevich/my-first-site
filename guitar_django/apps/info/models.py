from django.db import models

class Info(models.Model):
    title_message = models.CharField('Кратко о пожелании', max_length=200)
    message = models.TextField('Само пожелание или привет для пользователей')

    def __str__(self):
        return self.title_message

    class Meta:
        verbose_name = 'Добавить пожелание'
        verbose_name_plural = 'Добавить пожелания'
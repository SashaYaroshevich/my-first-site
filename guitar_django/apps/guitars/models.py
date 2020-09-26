from django.db import models

class Guitar(models.Model):
    guitar_title = models.CharField('Вид гитары', max_length = 200)
    guitar_text = models.TextField('Описание гитары')

    def __str__(self):
        return self.guitar_title
    class Meta:
        verbose_name = 'Гитару'
        verbose_name_plural = 'Гитары'


class Comment(models.Model):
    guitar = models.ForeignKey(Guitar, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


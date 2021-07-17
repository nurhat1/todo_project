from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    """ Task Model """
    title = models.CharField('Заголовок задачи', max_length=100)
    description = models.TextField('Описание задачи')
    deadline = models.DateTimeField('Срок исполнения', default=timezone.now)
    is_executed = models.BooleanField('Выполнено', default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'Задача {self.title}'

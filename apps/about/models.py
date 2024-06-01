from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название задачи',
        help_text='Введите название задачи',
    )
    description = models.TextField(
        verbose_name='Описание задачи',
        help_text='Введите описание задачи',
    )
    completed = models.BooleanField(
        default = False,
        verbose_name='Выполнена ли задача',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
    
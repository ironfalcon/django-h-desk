from django.db import models

# Create your models here.


class Item(models.Model):
    # task = models.ForeignKey(Task, on_delete = models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название')
    number = models.IntegerField(default=0, verbose_name='Колличество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class Task(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    items = models.ForeignKey(Item, on_delete=models.CASCADE, default='---', verbose_name='Оборудование')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

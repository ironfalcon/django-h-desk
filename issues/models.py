from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст Заявки')
    priority = models.ForeignKey('issues.Priority', on_delete=models.CASCADE, default='---', verbose_name='Приоритет')
    date_start = models.DateTimeField(verbose_name='Дата создания')
    date_end = models.DateTimeField(verbose_name='Дата закрытия', null=True)
    location = models.ForeignKey('issues.Place', on_delete=models.CASCADE, default='---', verbose_name='Местонахождение')
    status = models.ForeignKey('issues.Status', on_delete=models.CASCADE, default='---', verbose_name='Статус')
    assigned = models.CharField(max_length=50, default='---', verbose_name='Исполнитель')
    created = models.CharField(max_length=50, default='---', verbose_name='Создатель заявки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Priority(models.Model):
    priority_name = models.CharField(max_length=50, verbose_name='Приоритет')

    def __str__(self):
        return self.priority_name

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'
        ordering = ['id']


class Place(models.Model):
    name_place = models.CharField(max_length=50, verbose_name='Название комнаты')

    def __str__(self):
        return self.name_place

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Status(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

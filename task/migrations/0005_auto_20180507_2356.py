# Generated by Django 2.0.5 on 2018-05-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20180507_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='task',
        ),
        migrations.AddField(
            model_name='item',
            name='task',
            field=models.ManyToManyField(to='task.Task'),
        ),
    ]
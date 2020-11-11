# Generated by Django 3.0.11 on 2020-11-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20201111_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='boards',
        ),
        migrations.AddField(
            model_name='account',
            name='boards',
            field=models.ManyToManyField(blank=True, related_name='account_boards', to='tasks.Board'),
        ),
        migrations.RemoveField(
            model_name='account',
            name='tasks',
        ),
        migrations.AddField(
            model_name='account',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='account_tasks', to='tasks.Task'),
        ),
    ]
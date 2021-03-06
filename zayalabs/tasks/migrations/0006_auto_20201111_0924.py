# Generated by Django 3.0.11 on 2020-11-11 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_auto_20201111_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='board_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

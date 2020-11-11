# Generated by Django 3.0.11 on 2020-11-11 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_auto_20201111_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='board_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
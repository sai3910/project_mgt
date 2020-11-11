# Generated by Django 3.0.11 on 2020-11-11 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_auto_20201111_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('TODO', 'To Do'), ('IP', 'In Progress'), ('DONE', 'Done')], max_length=4)),
                ('attachements', models.FileField(upload_to='media/attachements/', verbose_name='attachement File')),
                ('accomplished_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accomplished_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='tasks.Board')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='list_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='list_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='card',
            name='card_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_list', to='tasks.List'),
        ),
        migrations.AddField(
            model_name='card',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='card_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]

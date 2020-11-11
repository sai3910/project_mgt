# Generated by Django 3.0.11 on 2020-11-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201110_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='account_membership', to='users.Membership'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
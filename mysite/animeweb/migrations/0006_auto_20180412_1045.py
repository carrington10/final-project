# Generated by Django 2.0.1 on 2018-04-12 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animeweb', '0005_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

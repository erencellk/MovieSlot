# Generated by Django 5.2.2 on 2025-06-24 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0017_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='username',
        ),
    ]

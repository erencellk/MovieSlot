# Generated by Django 5.2.2 on 2025-06-18 10:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_remove_actor_films_actor_films'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oscaraward',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2027)]),
        ),
    ]

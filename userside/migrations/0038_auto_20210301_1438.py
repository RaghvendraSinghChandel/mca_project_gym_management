# Generated by Django 3.1.5 on 2021-03-01 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0037_auto_20210301_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_type',
            name='type_id',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
    ]

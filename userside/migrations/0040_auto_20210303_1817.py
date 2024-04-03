# Generated by Django 3.1.5 on 2021-03-03 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0039_auto_20210303_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership_master',
            name='amount',
            field=models.IntegerField(help_text='Amount Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='tot_amt',
            field=models.IntegerField(help_text='Total Amount Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='trainer_details',
            name='salary',
            field=models.IntegerField(help_text='Salary of Trainer Must be less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='mname',
            field=models.CharField(help_text='Name of the User <br> Must Be Within 25 Characters <br> Enter Alphabets Only', max_length=25),
        ),
        migrations.AlterField(
            model_name='user_type',
            name='utype',
            field=models.CharField(help_text='Type of User', max_length=7),
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-25 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0014_workout_master_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_master',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
    ]

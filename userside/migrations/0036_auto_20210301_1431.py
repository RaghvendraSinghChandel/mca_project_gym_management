# Generated by Django 3.1.5 on 2021-03-01 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0035_auto_20210301_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_master',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
        migrations.AlterField(
            model_name='feedback_master',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
        migrations.AlterField(
            model_name='order_master',
            name='order_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order_master',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
        migrations.AlterField(
            model_name='trainer_details',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userside.user_master'),
        ),
    ]

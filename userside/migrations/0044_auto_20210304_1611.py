# Generated by Django 3.1.5 on 2021-03-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0043_auto_20210304_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_master',
            name='type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userside.user_type'),
        ),
    ]

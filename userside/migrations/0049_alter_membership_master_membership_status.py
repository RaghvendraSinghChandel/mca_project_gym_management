# Generated by Django 5.0.3 on 2024-03-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0048_alter_membership_master_membership_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership_master',
            name='membership_status',
            field=models.CharField(help_text='Membership Status', max_length=255),
        ),
    ]

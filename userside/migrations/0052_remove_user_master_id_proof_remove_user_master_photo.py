# Generated by Django 5.0.3 on 2024-03-24 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0051_delete_order_details_delete_product_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_master',
            name='id_proof',
        ),
        migrations.RemoveField(
            model_name='user_master',
            name='photo',
        ),
    ]
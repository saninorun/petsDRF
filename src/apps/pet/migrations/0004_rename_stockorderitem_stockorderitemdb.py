# Generated by Django 4.2.7 on 2023-11-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_alter_sellpricebd_discount_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockOrderItem',
            new_name='StockOrderItemDB',
        ),
    ]
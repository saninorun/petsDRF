# Generated by Django 4.2.7 on 2023-11-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet", "0002_alter_orderitembd_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderbd",
            name="number_order",
            field=models.PositiveIntegerField(null=True),
        ),
    ]

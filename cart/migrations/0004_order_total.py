# Generated by Django 4.2.7 on 2023-11-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

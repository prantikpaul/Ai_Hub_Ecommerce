# Generated by Django 4.2.7 on 2023-11-11 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_review',
            name='cmnt_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

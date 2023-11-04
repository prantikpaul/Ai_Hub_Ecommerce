# Generated by Django 4.2.7 on 2023-11-04 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0009_remove_save_quantity_alter_order_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
        migrations.AlterField(
            model_name='save',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]

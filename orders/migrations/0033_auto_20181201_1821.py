# Generated by Django 2.1.1 on 2018-12-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_orderinfo_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='menus.Product'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20181023_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='cart.CartItem'),
        ),
    ]

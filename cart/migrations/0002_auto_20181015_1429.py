# Generated by Django 2.1.1 on 2018-10-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_drink'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='menus.Salad'),
        ),
    ]

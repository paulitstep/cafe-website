# Generated by Django 2.1.1 on 2018-11-13 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20181113_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
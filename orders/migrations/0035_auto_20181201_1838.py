# Generated by Django 2.1.1 on 2018-12-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='ABC', max_length=120, verbose_name='ID заказа'),
        ),
    ]

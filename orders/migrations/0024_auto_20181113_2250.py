# Generated by Django 2.1.1 on 2018-11-13 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderInfo'),
        ),
    ]

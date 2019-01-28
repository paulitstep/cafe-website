# Generated by Django 2.1.1 on 2018-10-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20181029_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='menus.Variation'),
        ),
    ]
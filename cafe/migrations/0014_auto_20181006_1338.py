# Generated by Django 2.1.1 on 2018-10-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0013_auto_20181003_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='person_quantity',
            field=models.PositiveIntegerField(verbose_name='Количество людей'),
        ),
    ]

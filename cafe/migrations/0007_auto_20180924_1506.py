# Generated by Django 2.1.1 on 2018-09-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_auto_20180924_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='conditioner',
            field=models.CharField(max_length=10),
        ),
    ]

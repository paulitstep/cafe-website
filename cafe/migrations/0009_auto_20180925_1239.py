# Generated by Django 2.1.1 on 2018-09-25 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_auto_20180924_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата визита'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время визита'),
            preserve_default=False,
        ),
    ]
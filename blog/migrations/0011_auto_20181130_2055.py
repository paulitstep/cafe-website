# Generated by Django 2.1.1 on 2018-11-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181130_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]

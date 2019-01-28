# Generated by Django 2.1.1 on 2018-11-13 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0015_cart_cartitem'),
        ('orders', '0028_auto_20181113_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120, unique=True, verbose_name='ID заказа')),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Finished', 'Finished')], default='Started', max_length=120, verbose_name='Статус заказа')),
                ('price_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Итоговая сумма')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart', verbose_name='Корзина')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=120, verbose_name='Ваше имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Контактный телефон')),
                ('payment', models.CharField(choices=[('-', '-'), ('Наличными', 'Наличными'), ('Карточкой', 'Карточкой')], default='-', max_length=120, verbose_name='Оплата')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrderInfo'),
        ),
    ]

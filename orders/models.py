from django.db import models

from cart.models import Cart

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Finished', 'Finished'),
)

PAYMENT_CHOICES = (
    ('-', '-'),
    ('Наличными', 'Наличными'),
    ('Карточкой', 'Карточкой'),
)

class Order(models.Model):
    order_id = models.CharField(u"ID заказа", max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=u"Корзина")
    status = models.CharField(u"Статус заказа", max_length=120, choices=STATUS_CHOICES, default='Started')
    person_name = models.CharField(u"Ваше имя", max_length=120)
    phone = models.CharField(u"Контактный телефон", max_length=20)
    payment = models.CharField(u"Оплата", max_length=120, choices=PAYMENT_CHOICES, default='-')
    address = models.CharField(u"Адрес", max_length=120)
    comment = models.TextField(u"Комментарии", blank=True, null=True)

    def __str__(self):
        return self.order_id
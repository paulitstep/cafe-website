from PIL import Image
from django.db import models
from django.utils import timezone

class Cafe(models.Model):
    image = models.ImageField(blank=True, null=True)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    conditioner = models.CharField(max_length=10)

    def __str__(self):
        return self.district

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Booking(models.Model):
    district = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name=u"Район")
    person_name = models.CharField(u"Ваше имя", max_length=50)
    date = models.DateField(u"Дата визита")
    time = models.CharField(u"Время визита", max_length=20)
    person_quantity = models.PositiveIntegerField(u"Количество людей")
    phone = models.CharField(u"Контактный телефон", max_length=20)
    comment = models.TextField(u"Комментарий", blank=True, null=True)
    created_at = models.DateTimeField(u"Время отправки", default=timezone.now)

    def __str__(self):
        return self.phone
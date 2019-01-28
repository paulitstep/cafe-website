from PIL import Image
from django.db import models
from django.urls import reverse


class Product(models.Model):
    category = models.CharField(max_length=150)
    image = models.ImageField()
    name = models.CharField(max_length=150)
    components = models.TextField()
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField(blank=True, null=True, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'slug')

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
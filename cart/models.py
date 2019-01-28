from django.db import models

from menus.models import Product

class Cart(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    available = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.name
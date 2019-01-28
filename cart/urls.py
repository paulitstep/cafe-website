from django.urls import path

from cart.views import CartView, add_to_cart, remove_from_cart

urlpatterns = [
    path('', CartView, name='cart_view'),
    path('<slug>/', add_to_cart, name='add_to_cart'),
    path('(<id>\d+)', remove_from_cart, name='remove_from_cart'),
]

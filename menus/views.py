from django.views.generic import ListView

from .models import Product


class PizzaListView(ListView):
    queryset = Product.objects.filter(category__iexact='Pizza', available=True)
    template_name = 'menus/pizza_list.html'


class SaladListView(ListView):
    queryset = Product.objects.filter(category__iexact='Salad', available=True)
    template_name = 'menus/salad_list.html'

class Hot_MealListView(ListView):
    queryset = Product.objects.filter(category__iexact='Hot_meal', available=True)
    template_name = 'menus/hot_meal_list.html'

class DrinkListView(ListView):
    queryset = Product.objects.filter(category__iexact='Drink', available=True)
    template_name = 'menus/drink_list.html'
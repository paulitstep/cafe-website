from django.urls import path

from menus.views import PizzaListView, SaladListView, Hot_MealListView, DrinkListView



urlpatterns = [
    path('pizza/', PizzaListView.as_view(), name='pizza'),
    path('salad/', SaladListView.as_view(), name='salad'),
    path('hot_meal/', Hot_MealListView.as_view(), name='hot_meal'),
    path('drink/', DrinkListView.as_view(), name='drink'),
]

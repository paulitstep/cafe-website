from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from cart.models import Cart
from orders.forms import OrderCreateForm

from orders.models import Order

def order(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart_view'))

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_id = the_id
            order.cart = cart
            order.save()

    try:
        new_order = Order.objects.get(cart=cart)
        messages.success(request, 'Спасибо за заказ! Ваш заказ №{}. Скоро с Вами свяжется наш менеджер.'.format(the_id))
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect('/')
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.order_id = the_id
        new_order.save()
        messages.success(request, 'Спасибо за заказ! Ваш заказ №{}. Скоро с Вами свяжется наш менеджер.'.format(the_id))
        del request.session['cart_id']
        del request.session['items_total']
    except:
        return HttpResponseRedirect(reverse('cart_view'))

    if new_order.status == 'Finished':
        cart.delete()
        return HttpResponseRedirect(reverse('cart_view'))

    context = {}
    template_name = 'base.html'
    return render(request, template_name, context)
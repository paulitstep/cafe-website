import decimal
from decimal import Decimal

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from menus.models import Product
from orders.forms import OrderCreateForm

from .models import Cart, CartItem

def CartView(request):
    form = OrderCreateForm(request.POST or None)

    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * (item.quantity)
            new_total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {'cart': cart, 'form': form}
    else:
        empty_message = 'ВАША КОРЗИНА ПУСТА'
        context = {'empty': True, 'empty_message': empty_message}

    template = 'cart/detail.html'
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart1 = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart_view'))

    cartitem = CartItem.objects.get(id=id)
    cartitem.cart = None
    cartitem.save()
    return HttpResponseRedirect(reverse('cart_view'))

def add_to_cart(request, slug):
    request.session.set_expiry(120000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    if request.method == 'POST':
        qty = request.POST['qty']

        cart_item = CartItem.objects.create(cart=cart, product=product)

        cart_item.quantity = qty
        cart_item.save()

        return HttpResponseRedirect(reverse('cart_view'))


    return HttpResponseRedirect(reverse('cart_view'))
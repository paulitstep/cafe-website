from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from menus.models import Product
from .forms import Booking_Form
from .models import Cafe

def cafe_view(request):
    form = Booking_Form(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Столик успешно забронирован!')
        return HttpResponseRedirect('/')
    queryset = Cafe.objects.all()
    template_name = 'cafe/cafe_list.html'
    context = {'object_list': queryset, 'form': form}
    return render(request, template_name, context)
from django.shortcuts import render

from cars.forms import FilterForm
from cars.models import Car, Image
from cart.cart import Cart


def car_list(request, pk=None):
    context = {}
    cart = Cart(request)
    context['cars'] = Car.objects.all()
    context['ordered'] = Car.objects.filter(id__in=cart.get_items())
    context['number'] = len(cart)
    context['total'] = cart.get_total_price()
    context['form'] = FilterForm

    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        # context['cars'] = Car.objects.all()

    if pk is None:
        return render(request, 'cars/car_list.html', context)

    else:
        car = Car.objects.get(id=pk)
        context['car'] = car
        context['gallery'] = Image.objects.filter(car=car)
        return render(request, 'cars/car_detail.html', context)

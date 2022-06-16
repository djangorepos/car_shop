from django.shortcuts import render
from cars.models import Car
from cart.cart import Cart


def car_list(request, pk=None):
    context = {}
    cart = Cart(request)
    context['cars'] = Car.objects.all()
    context['ordered'] = Car.objects.filter(id__in=cart.get_items())
    context['number'] = len(cart)
    context['total'] = cart.get_total_price()

    if pk is None:
        return render(request, 'cars/car_list.html', context)

    else:
        context['car'] = Car.objects.get(id=pk)
        return render(request, 'cars/car_detail.html', context)

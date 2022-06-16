from django.shortcuts import render
from cars.models import Car, Image
from cart.cart import Cart


def car_list(request, pk=None):
    context = {}
    cart = Cart(request)
    context['cars'] = Car.objects.all()
    context['ordered'] = Car.objects.filter(id__in=cart.get_items())
    context['number'] = len(cart)
    context['total'] = cart.get_total_price()

    if request.method == 'POST':
        pass

        # context['cars'] = Car.objects.all()

    if pk is None:
        return render(request, 'cars/car_list.html', context)

    else:
        car = Car.objects.get(id=pk)
        context['car'] = car
        context['gallery'] = Image.objects.filter(car=car)
        return render(request, 'cars/car_detail.html', context)

from django.shortcuts import render
from cars.models import Car
from cart.cart import Cart


def car_list(request):
    products = Car.objects.all()
    cart = Cart(request)
    number = len(cart)
    ordered = Car.objects.filter(id__in=cart.get_items())
    total = cart.get_total_price()
    return render(request, 'cars/car_list.html', {'products': products,
                                                  'ordered': ordered,
                                                  'number': number,
                                                  'total': total})


def car_detail(request, pk):
    product = Car.objects.get(id=pk)
    return render(request, 'cars/car_detail.html', {'product': product})

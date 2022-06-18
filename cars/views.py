from django.http import HttpResponse
from django.shortcuts import render

from cars.forms import FilterForm
from cars.models import Car, Image
from cart.cart import Cart


def cars_list(request, pk=None):
    context = {}
    cart = Cart(request)
    cars = Car.objects.filter(ordered=False)
    context['cars'] = cars
    context['ordered'] = Car.objects.filter(id__in=cart.get_items())
    context['number'] = len(cart)
    context['total'] = cart.get_total_price()
    context['form'] = FilterForm

    if request.method == 'POST':
        print(request.POST)

        if request.POST.get('make') != 'All makes':
            cars = cars.filter(make=request.POST.get('make')).order_by('model')

        if request.POST.get('body_style') != 'All styles':
            cars = cars.filter(body_style=request.POST.get('body_style')).order_by('model')

        if request.POST.get('fuel_type') != 'All types':
            cars = cars.filter(engine__fuel_type=request.POST.get('fuel_type')).order_by('model')

        if request.POST.get('model') != 'All models':
            cars = cars.filter(model=request.POST.get('model'))

        context['cars'] = cars
        return render(request, 'cars/car_list.html', context)

    if pk is None:
        return render(request, 'cars/car_list.html', context)

    else:
        car = Car.objects.get(id=pk)
        context['car'] = car
        context['gallery'] = Image.objects.filter(car=car)
        return render(request, 'cars/car_detail.html', context)


def cars_search(request):
    cars = Car.objects.filter(ordered=False)

    if request.GET.get('make') != 'All makes':
        cars = cars.filter(make=request.GET.get('make')).order_by('model')

    if request.GET.get('body_style') != 'All styles':
        cars = cars.filter(body_style=request.GET.get('body_style')).order_by('model')

    if request.GET.get('fuel_type') != 'All types':
        cars = cars.filter(engine__fuel_type=request.GET.get('fuel_type')).order_by('model')

    data = ''

    for car in cars:
        data += f"<option value='{car.model}'>{car.model}</option>"

    return HttpResponse(data)

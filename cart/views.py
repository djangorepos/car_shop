from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cars.forms import OrderForm, OrderedCarForm
from cars.models import Car, Feature, Engine
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Car, id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(product=product)
    return redirect('car_list')


@require_POST
def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Car, id=pk)
    cart.remove(product)
    return redirect('car_list')


def cart_order(request):
    context = {}
    cart = Cart(request)
    ordered = Car.objects.filter(id__in=cart.get_items())
    number = len(ordered)
    OrderFormSet = formset_factory(OrderedCarForm, extra=number)
    formset = OrderFormSet()
    form = OrderForm()
    context['ordered'] = ordered
    context['number'] = number
    context['total'] = cart.get_total_price()
    context['formset'] = formset
    context['form'] = form
    return render(request, 'cars/cart_order.html', context)


def cart_engine(request):
    price = Car.objects.get(id=request.GET.get('car')).price
    price -= Engine.objects.get(id=request.GET.get('car_engine')).price
    price += Engine.objects.get(id=request.GET.get('selected_engine')).price

    return HttpResponse(price)


def cart_features(request):
    price = float(request.GET.get('price'))

    if request.GET.get('checked') == 'true':
        price += Feature.objects.get(id=request.GET.get('feature')).price
    else:
        price -= Feature.objects.get(id=request.GET.get('feature')).price

    return HttpResponse(price)

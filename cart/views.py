from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cars.models import Car
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

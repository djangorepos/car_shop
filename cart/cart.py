import random
from django.conf import settings
from cars.models import Car


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Car.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

    def __len__(self):
        return len(self.cart.values())

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(float(item['price']) for item in self.cart.values())

    def get_items(self):
        return self.cart.keys()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

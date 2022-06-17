"""car_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from car_shop import settings
from cars.views import car_list, car_search
from cart.views import cart_add, cart_remove, cart_order, cart_engine, cart_features, cart_contact

urlpatterns = [
    path('', car_list, name='car_list'),
    path('car/<pk>', car_list, name='car_detail'),
    path('car/search', car_search, name='car_search'),
    path('add/<pk>', cart_add, name='cart_add'),
    path('remove/<pk>', cart_remove, name='cart_remove'),
    path('cart/engine', cart_engine, name='cart_engine'),
    path('cart/features', cart_features, name='cart_features'),
    path('order/', cart_order, name='cart_order'),
    path('order/contacts', cart_contact, name='cart_contacts'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
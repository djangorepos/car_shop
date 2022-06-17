from django.contrib import admin

from cars.models import *


class ImageInline(admin.TabularInline):
    fk_name = 'car'
    model = Image


@admin.register(Car)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Engine)
admin.site.register(Feature)
admin.site.register(Order)
admin.site.register(OrderedCar)
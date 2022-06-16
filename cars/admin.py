from django.contrib import admin

from cars.models import Image, Car, Feature


class ImageInline(admin.TabularInline):
    fk_name = 'car'
    model = Image


@admin.register(Car)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Feature)

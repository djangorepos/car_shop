from django.contrib import admin

from cars.models import Image, Car, Engine, Feature


class ImageInline(admin.TabularInline):
    fk_name = 'car'
    model = Image


@admin.register(Car)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Engine)
admin.site.register(Feature)

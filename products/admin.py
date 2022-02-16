"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'number_id',
        'name',
        'category',
        'brand',
        'price',
        'rating',
        'image_url',
    )

    ordering = ('number_id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

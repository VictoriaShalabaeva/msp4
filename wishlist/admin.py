from django.contrib import admin
from .models import Wishlist

# Register your models here.

class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        # 'number_id',
        # 'name',
        'product_color',
        # 'price'
    )

admin.site.register(Wishlist, WishlistAdmin)

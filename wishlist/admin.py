# from django.contrib import admin
# from .models import Wishlist

# # Register your models here.

# class WishlistAdmin(admin.ModelAdmin):
#     list_display = (
#         'user_profile',
#         'product',
#         'product_color',
#     )

# admin.site.register(Wishlist, WishlistAdmin)


from django.contrib import admin
from .models import Wishlist, WishlistLineItem


class WishlistLineItemAdminInline(admin.TabularInline):
    model = WishlistLineItem


class WishlistAdmin(admin.ModelAdmin):
    inlines = (WishlistLineItemAdminInline,)

    fields = ('user_profile',)

    list_display = ('user_profile',)

admin.site.register(Wishlist, WishlistAdmin)


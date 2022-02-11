from django.contrib import admin
from .models import Wishlist, WishlistLineItem


class WishlistLineItemAdminInline(admin.TabularInline):
    model = WishlistLineItem


class WishlistAdmin(admin.ModelAdmin):
    inlines = (WishlistLineItemAdminInline,)

    fields = ('user',)

    list_display = ('user',)

admin.site.register(Wishlist, WishlistAdmin)


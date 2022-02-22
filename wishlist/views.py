"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist, WishlistLineItem
from products.models import Product
from profiles.models import UserProfile


@login_required
def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    user_wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = WishlistLineItem.objects.filter(wishlist=user_wishlist)
    
    return render(request, 'wishlist/wishlist.html',
                  {"wishlist_items": wishlist_items})


@login_required
def add_to_wishlist(request, item_id):
    """ Add products to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    user_wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        product_wishlisted = False
        if color:
            product_wishlisted = WishlistLineItem.objects.filter(
                wishlist=user_wishlist, product=product,
                product_color=color).exists()
        else:
            product_wishlisted = WishlistLineItem.objects.filter(
                wishlist=user_wishlist, product=product).exists()

        if product_wishlisted:
            messages.warning(request, 'Product is already in your wishlist.')
        else:
            wishlist_item = WishlistLineItem.objects.create(
                wishlist=user_wishlist, product=product, product_color=color)
            messages.success(
                request, f'Added {product.name} ({color}) to your wishlist.')

    return redirect(redirect_url)


@login_required
def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    color = None

    if 'product_color' in request.POST:
        color = request.POST['product_color']

    user_wishlist = Wishlist.objects.get(user=request.user)

    if request.method == 'POST':
        product_wishlisted = False
        if color:
            product_wishlisted = WishlistLineItem.objects.get(
                wishlist=user_wishlist, product=product,
                product_color=color)
            product_wishlisted.delete()
            messages.success(
                request, f'Removed {product.name} \
                    ({color}) from your wishlist')

        else:
            product_wishlisted = WishlistLineItem.objects.get(
                wishlist=user_wishlist, product=product)
            product_wishlisted.delete()
            messages.success(
                request, f'Removed {product.name} from your wishlist')

        return redirect(redirect_url)

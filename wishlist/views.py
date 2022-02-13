from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist, WishlistLineItem
from products.models import Product
from profiles.models import UserProfile

# Create your views here.

@login_required
def view_wishlist(request):
    """ A view that renders the wishlist contents page """
    user_wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist_items = WishlistLineItem.objects.filter(wishlist=user_wishlist)
    # user_wishlist = Wishlist.objects.get_or_create(request.user)

    return render(request, 'wishlist/wishlist.html', {"wishlist_items": wishlist_items})


@login_required
def add_to_wishlist(request, item_id):
    """ Add products to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    user_wishlist, _ = Wishlist.objects.get_or_create(request.user)

    # wishlist_items = {
    #     wishlist_item.product.id: wishlist_item
    #     for wishlist_item in WishlistLineItem.objects.filter(wishlist=user_wishlist)
    # }


    if request.method == 'POST':
        product_wishlisted = False
        if color:
            product_wishlisted = WishlistLineItem.objects.filter(wishlist=user_wishlist, product=product, product_color=color).exists()
        else:
            product_wishlisted = WishlistLineItem.objects.filter(wishlist=user_wishlist, product=product).exists()

        if product_wishlisted:
            # wishlist_item = wishlist_items[product.id]
            # if wishlist_item.product_color == color:
                messages.warning(request, 'Product already in wishlit.')
        else:
            wishlist_item = WishlistLineItem.objects.create(
                wishlist=user_wishlist, product=product,product_color=color)
            # user_wishlist.products.add(wishlist_item)
            messages.success(request, f'Added {product.name} ({color}) to wishlist.')

    


        # if color:
        #     if item_id in list(user_wishlist.keys()):
        #         if color in user_wishlist[item_id]['items_by_color'].keys():
        #             user_wishlist[item_id]['items_by_color'][color] += quantity
        #         else:
        #             user_wishlist[item_id]['items_by_color'][color] = quantity
        #             messages.success(request, f'Added color {color} {product.name} to your user_wishlist')
        #     else:
        #         user_wishlist[item_id] = {'items_by_color': {color: quantity}}
        #         messages.success(request, f'Added color {color} {product.name} to your user_wishlist')
        # else:
        #     if item_id in list(user_wishlist.keys()):
        #         user_wishlist[item_id] += quantity
        #         messages.success(request, f'Updated {product.name} quantity to {user_wishlist[item_id]}')
        #     else:
        #         user_wishlist[item_id] = quantity
        #         messages.success(request, f'Added {product.name} to your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        wishlist = Wishlist.objects.get_or_create('wishlist', {})

        if color:
            del wishlist[item_id]['items_by_color'][color]
            if not wishlist[item_id]['items_by_color']:
                wishlist.pop(item_id)
            messages.success(request, f'Removed color {color} {product.name} from your wishlist')
        else:
            wishlist.pop(item_id)
            messages.success(request, f'Removed {product.name} from your wishlist')

        #request.session['wishlist'] = wishlist
        return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

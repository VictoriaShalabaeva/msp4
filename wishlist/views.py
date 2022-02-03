from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add products to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    wishlist = request.session.get('wishlist', {})

    if color:
        if item_id in list(wishlist.keys()):
            if color in wishlist[item_id]['items_by_color'].keys():
                wishlist[item_id]['items_by_color'][color] += quantity
            else:
                wishlist[item_id]['items_by_color'][color] = quantity
                messages.success(request, f'Added color {color} {product.name} to your wishlist')
        else:
            wishlist[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request, f'Added color {color} {product.name} to your wishlist')
    else:
        if item_id in list(wishlist.keys()):
            wishlist[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {wishlist[item_id]}')
        else:
            wishlist[item_id] = quantity
            messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        wishlist = request.session.get('wishlist', {})

        if color:
            del wishlist[item_id]['items_by_color'][color]
            if not wishlist[item_id]['items_by_color']:
                wishlist.pop(item_id)
            messages.success(request, f'Removed color {color} {product.name} from your wishlist')
        else:
            wishlist.pop(item_id)
            messages.success(request, f'Removed {product.name} from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

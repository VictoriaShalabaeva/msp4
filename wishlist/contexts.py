from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def wishlist_contents(request):

    wishlist_items = []
    total = 0
    product_count = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            wishlist_items.append({
                'item_id': item_id,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for color in item_data['items_by_color'].items():
                wishlist_items.append({
                    'item_id': item_id,
                    'product': product,
                    'color': color,
                })
    
    context = {
        'wishlist_items': wishlist_items,
    }

    return context
# from django.conf import settings
# from django.shortcuts import get_object_or_404
# from products.models import Product


# def wishlist_contents(request):

#     wishlist_items = []
#     # total = 0
#     product_count = 0
#     wishlist = None
#     try:
#         wishlist = Wishlist.objects.get(user=request.user)
#     except Wishlist.DoesNotExist:
#         pass

#     for item_id, item_data in wishlist.items():
#         if isinstance(item_data, int):
#             product = get_object_or_404(Product, pk=item_id)
#             # total += item_data * product.price
#             product_count += item_data
#             wishlist_items.append({
#                 'item_id': item_id,
#                 'quantity': item_data,
#                 'product': product,
#             })
#         else:
#             product = get_object_or_404(Product, pk=item_id)
#             for color, quantity in item_data['items_by_color'].items():
#                 # total += quantity * product.price
#                 product_count += quantity
#                 wishlist_items.append({
#                     'item_id': item_id,
#                     'quantity': quantity,
#                     'product': product,
#                     'color': color,
#                 })
    
#     context = {
#         'wishlist_items': wishlist_items,
#         'product_count': product_count,
#     }

#     return context
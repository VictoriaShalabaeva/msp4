# from django.db import models
# from products.models import Product
# from profiles.models import UserProfile

# # Create your models here.

# class Wishlist(models.Model):
#     """
#     Wishlist model to allow user to create a wishlist
#     """
#     user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_color = models.CharField(max_length=254, null=True, blank=True)

#     def __str__(self):
#         return self.user_profile


from django.db import models


from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='wishlist')

    def __str__(self):
        return str(self.id)


class WishlistLineItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_color = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return str(self.id)


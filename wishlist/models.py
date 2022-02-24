"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    Model to show all product items within the users wishlist
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wishlist",
    )
    products = models.ManyToManyField(
        Product, through="WishlistLineItem", related_name="product_wishlists"
    )

    def __str__(self):
        return f"Wishlist ({self.user})"


class WishlistLineItem(models.Model):
    """
    Model to allow users to add
    individual products to their wishlist.
    """

    wishlist = models.ForeignKey(
        Wishlist,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    product_color = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return self.product.name

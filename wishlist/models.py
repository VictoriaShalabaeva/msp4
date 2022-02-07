from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.

class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='wishlist')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_color = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user_profile

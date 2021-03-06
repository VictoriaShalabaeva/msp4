"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    number_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    product_colors = models.JSONField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    price_sign = models.CharField(max_length=254, null=True, blank=True)
    currency = models.CharField(max_length=254, null=True, blank=True)
    product_link = models.URLField(max_length=1024, null=True, blank=True)
    website_link = models.URLField(max_length=1024, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    type_category = models.CharField(max_length=254, null=True, blank=True)
    tag_list = models.JSONField(null=True, blank=True)
    created_at = models.CharField(max_length=500, null=True, blank=True)
    updated_at = models.CharField(max_length=500, null=True, blank=True)
    product_api_url = models.URLField(max_length=1024, null=True, blank=True)
    api_featured_image = models.URLField(
        max_length=1024, null=True, blank=True
    )

    def __str__(self):
        return self.name

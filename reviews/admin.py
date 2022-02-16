"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'product',
        'user',
        'date_posted'
    )

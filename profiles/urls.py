"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]

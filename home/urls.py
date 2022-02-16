"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

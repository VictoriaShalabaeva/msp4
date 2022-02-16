"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

"""Code credit: the code is written following the Code Institute tutorials
(Boutique Ado Project).
"""

from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

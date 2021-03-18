from django.contrib import admin
from .models import Order
from cart.models import Cart, CartItem


admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
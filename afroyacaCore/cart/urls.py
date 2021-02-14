from django.urls import path
from . import views


urlpatterns = [
    path('add/product/<str:slug>', views.add_product, name="cart_add_product"),
    path('my', views.cart_view, name="my_cart"),
    path('remove/item', views.remove_item, name="remove_cart_item"),
]

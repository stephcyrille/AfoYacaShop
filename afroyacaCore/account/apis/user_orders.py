# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from checkout.models import Order
from cart.models import CartItem

exclude_fields = ["is_archived", "created_by", "modified_by", "modified_date", "is_published"]


class MyOrderSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def get_contact(self, instance):
        contact = ''
        if instance.contact:
            contact = instance.contact.address
        return contact

    def get_products(self, instance):
        cart_items = []
        cart = instance.cart
        if cart is not None:
            ci = CartItem.objects.filter(cart=cart)

            for i in ci:
                product = {
                    "ref": i.variety.product.ref,
                    "title": i.variety.product.title,
                    "price": i.variety.product.price,
                    "quantity": i.quantity,
                }
                cart_items.append(product)
        return cart_items

    class Meta:
        model = Order
        exclude = exclude_fields


class UserOrderAPIView(APIView):
    queryset = Order.objects.none()
    serializer_class = MyOrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, request):
        user = request.user
        return Order.objects.filter(is_archived=False, user=user.userprofile)

    def get(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset(request)
        serializer = MyOrderSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

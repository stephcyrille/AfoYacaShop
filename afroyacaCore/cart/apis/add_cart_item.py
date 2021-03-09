from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from cart.models import CartItem, Cart
from products.models import Variety

exclude_fields = ["is_archived", "created_by", "modified_by", "created_date", "modified_date"]


class CartItemPostSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = CartItem
        exclude = exclude_fields


class AddCartItemAPIView(APIView):

    def post(self, request):
        serializer = CartItemPostSerializer(data=request.data['data'])
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        request.session.set_expiry(120000)

        try:
            the_id = request.session['cart_id']
        except Exception as e:
            print("No cart then, create a new cart for the purpose")
            print("Here is the exception when catching cart id from session", e.__str__())
            new_cart = Cart()
            new_cart.save()
            request.session['cart_id'] = new_cart.id
            the_id = new_cart.id

        cart = Cart.objects.get(id=the_id)

        quantity = int(data['quantity'])
        variety = Variety.objects.get(id=data["variety"])
        variety_price = variety.product.price
        line_total = variety_price * quantity
        cart_items_by_variety = CartItem.objects.filter(variety=variety, cart=cart, is_archived=False)

        if not cart_items_by_variety:
            cart_item = CartItem(cart=cart, variety=variety, quantity=quantity,
                                 line_total=line_total, is_archived=False)
            cart_item.save()
        else:
            c_item = cart_items_by_variety.first()
            c_item.quantity = c_item.quantity + quantity
            c_item.save()
            # Change also variety item quantity because when cart_item save, the quantity of variety must decrease
            previous_variety_quantity = variety.quantity
            new_variety_quantity = previous_variety_quantity - quantity
            variety.quantity = new_variety_quantity
            variety.save()

        response = {
            "message": "Item add with success"
        }
        return Response(response, status=status.HTTP_201_CREATED)

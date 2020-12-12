from cart.models import Cart, CartItem


def cart_items_number(request):
    try:
        cart_id = request.session["cart_id"]
        cart = Cart.objects.get(id=cart_id)
        cart_items = CartItem.objects.filter(cart=cart, is_archived=False)
        total_quantity = 0
        for i in cart_items:
            quantity = i.quantity
            total_quantity = total_quantity + quantity
    except Exception as e:
        total_quantity = 0

    context = {
        "cart_items_quantity": total_quantity,
        "favourite_items_quantity": 0
    }
    return context

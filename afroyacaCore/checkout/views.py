from django.shortcuts import render

from cart.models import Cart, CartItem


def checkout(request):
    template_name = "checkout/checkout.html"
    context = {}

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
        cart_items = CartItem.objects.filter(cart=cart, is_archived=False)
    except Exception as e:
        print("No cart found on session ", e.__str__())
        the_id = None

    if the_id:
        empty = False
        new_total = 0.00
        for item in cart_items:
            line_total = item.line_total
            new_total += line_total
        request.session['items_total'] = cart.cart_quantity()
        cart.total = new_total
        cart.save()
        context = {
            "cart": cart,
            "cart_items": cart_items
        }
    else:
        empty = True
        empty_message = "Votre panier est vide."
        cart = []
        cart_items = []
        context = {
            "cart": cart,
            "cart_items": cart_items
        }

    return render(request, template_name, context)
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from cart.models import Cart, CartItem
from products.models import Product, Variety


def add_product(request, slug):
    request.session.set_expiry(120000)
    print("Request POSTED VALUE HERE/////////", request.POST)

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

    try:
        product = Product.objects.get(slug=slug)
    except Exception as e:
        print("Exception here ", e.__str__())

    if request.method == "POST":
        quantity = int(request.POST['quantity'])
        variety = Variety.objects.get(id=request.POST['variety_id'])
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
        # success message
        return redirect(reverse('single_product', args=(slug,)))
    # error message
    return redirect(reverse('single_product', args=(slug,)))


def cart_view(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
        cart_items = CartItem.objects.filter(cart=cart, is_archived=False)
    except Exception as e:
        print("No cart found on session ", e.__str__())
        the_id = None

    try:
        del request.session['checkout_step']
    except Exception as e:
        print("No checkout step initialized ", e.__str__())

    try:
        del request.session['order_id']
    except Exception as e:
        print("No order session id initialized ", e.__str__())

    if the_id:
        empty = False
        new_total = 0.00
        for item in cart_items:
            line_total = item.line_total
            new_total += line_total
        request.session['items_total'] = cart.cart_quantity()
        cart.total = new_total
        cart.save()
        context = {"cart": cart, "cart_items": cart_items}
    else:
        empty = True
        empty_message = "Votre panier est vide."
        cart = []
        cart_items = []
        context = {
            "empty": empty,
            "empty_message": empty_message,
            "cart": cart,
            "cart_items": cart_items
        }

    template_name = 'cart/cart.html'
    return render(request, template_name, context)


def remove_item(request):
    print("Request POSTED VALUE HERE/////////", request.POST)
    cart_id = request.session['cart_id']
    if request.method == "POST":
        cart_item_id = request.POST['cart_item_id']
        try:
            cart_item = CartItem.objects.get(pk=cart_item_id)
            cart_item.is_archived = True
            try:
                # Update cart total quantity
                cart = Cart.objects.get(pk=cart_id)
                new_total = cart.total - cart_item.line_total
                cart.total = new_total
                cart.save()
                cart_item.save()
                # TODO flash messages success here
                return redirect(reverse('my_cart'))
            except Exception as e:
                print("Exception on getting cart from cart id", e.__str__())
                # TODO flash messages error here
                return redirect(reverse('my_cart'))
        except Exception as e:
            print("Exception on getting cart item", e.__str__())
            # TODO flash messages error here
            return redirect(reverse('my_cart'))

    return redirect(reverse('my_cart'))
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from account.models import Contact
from cart.models import Cart, CartItem

@login_required
def checkout(request):
    template_name = "checkout/checkout.html"
    contacts_list = Contact.objects.filter(is_archived=False)
    try:
        contacts = contacts_list[:2]
    except Exception as e:
        print("List is empty, contact not souscriptable!! ", e.__str__())
        contacts = []

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
        cart_items = CartItem.objects.filter(cart=cart, is_archived=False)
    except Exception as e:
        print("No cart found on session ", e.__str__())
        the_id = None
        return redirect(reverse('home'))

    if the_id:
        new_total = 0.00
        for item in cart_items:
            line_total = item.line_total
            new_total += line_total
        request.session['items_total'] = cart.cart_quantity()
        cart.total = new_total
        cart.save()
        context = {
            "cart": cart,
            "cart_items": cart_items,
        }
    else:
        cart = []
        cart_items = []
        context = {
            "cart": cart,
            "cart_items": cart_items
        }

    context["contacts"] = contacts
    return render(request, template_name, context)
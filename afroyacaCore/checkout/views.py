from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from account.models import Contact
from cart.models import Cart, CartItem
from .models import Order


@login_required
def checkout(request):
    template_name = "checkout/checkout.html"
    contacts_list = Contact.objects.filter(profile=request.user.userprofile, is_archived=False)

    try:
        contacts = contacts_list[:2]
    except Exception as e:
        print("List is empty, contact not souscriptable!! ", e.__str__())
        contacts = []

    # Getting only 2 contacts for the connected user
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
        cart_items = CartItem.objects.filter(cart=cart, is_archived=False)

        if len(cart_items) == 0:
            return redirect(reverse('home'))
    except Exception as e:
        print("No cart found on session ", e.__str__())
        the_id = None
        return redirect(reverse('home'))

    # Getting cart id
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

    try:
        step = request.session['checkout_step']
    except Exception as e:
        print("No step initialized on the current session ", e.__str__())
        step = 1
        request.session['checkout_step'] = step

    active_user = request.user.userprofile
    active_cart = cart
    try:
        active_contact = contacts_list.get(main=True)
    except Exception as e:
        active_contact = {}
        print('No main contact found ', e.__str__())
    status = "initialized"
    subtotal = cart.total
    tax_total = 0
    delivery_fees = 0
    final_total = subtotal + tax_total + delivery_fees

    try:
        order_id = request.session['order_id']
        session_order = Order.objects.get(id=order_id)
    except Exception as e:
        print('No order id found', e.__str__())
        session_order = Order(
                    user=active_user,
                    cart=active_cart,
                    contact=active_contact,
                    status=status,
                    sub_total=subtotal,
                    tax_total=tax_total,
                    delivery_fees=delivery_fees,
                    final_total=final_total,
                    payment_method='pay_to_go'
                  )
        session_order.save()
        request.session['order_id'] = session_order.id

    # Proceed all operations on checkout stepper ther
    if request.method == "POST":
        print("POSTED VALUES", request.POST, request.session['checkout_step'])

        # step += 1
        # request.session['checkout_step'] = step
        try:
            if "Suivant" == request.POST['next']:
                if step == 1:
                    step += 1
                    request.session['checkout_step'] = step
                elif 2 == step:
                    if "payment" in request.POST:
                        payment = request.POST['payment']
                        print("MY PAAAAAAAAAAAAAAYYYYYYYYYYMÂNT", payment, session_order.payment_method)
                        session_order.payment_method = payment
                        session_order.save()
                        step += 1
                        request.session['checkout_step'] = step
                else:
                    print("BERRRRRRRRRRRR NO STEP INCREASING")
        except:
            pass

        try:
            if "Précédent" == request.POST['previous']:
                if 1 == step:
                    return redirect(reverse('my_cart'))
                else:
                    step -= 1
                    request.session['checkout_step'] = step
                    print("KKKKAAAAAAAAAAAABOOOOOOUUUUUUUUUUUUUUUUUUU")
        except:
            pass

        try:
            if "Suivre ma commande" == request.POST['next']:
                del request.session['checkout_step']
                del request.session['cart_id']
                del request.session['order_id']
                return redirect(reverse('home'))
        except:
            pass

        try:
            if "Terminer" == request.POST['next']:
                del request.session['checkout_step']
                del request.session['cart_id']
                del request.session['order_id']
                session_order.status = 'confirmed'
                session_order.save()
                return redirect(reverse('home'))
        except:
            pass

    dim_contact = len(contacts)
    context["contacts"] = contacts
    context["dim_contact"] = dim_contact
    context["step"] = step
    return render(request, template_name, context)
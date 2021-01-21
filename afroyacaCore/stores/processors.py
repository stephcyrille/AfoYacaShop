import random
from cart.models import Cart, CartItem
from products.models import Product, Group
from settings.models import MainMenuNavPicture


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

    # Only get fours randomly
    trending_products = list(Product.objects.filter(is_archived=False))
    trending = random.sample(trending_products, 4)
    clothing_groups = Group.objects.filter(category__slug="vetements")
    shoes_groups = Group.objects.filter(category__slug="chaussures")
    bags_groups = Group.objects.filter(category__slug="sacs")
    accessories_groups = Group.objects.filter(category__slug="accessoires")
    jewelries_groups = Group.objects.filter(category__slug="bijoux")
    beauty_groups = Group.objects.filter(category__slug="beaute")

    main_nav_pic = MainMenuNavPicture.objects.filter().first()

    context = {
        "cart_items_quantity": total_quantity,
        "favourite_items_quantity": 0,
        "trending_products": trending,
        "clothing_groups": clothing_groups,
        "shoes_groups": shoes_groups,
        "bags_groups": bags_groups,
        "accessories_groups": accessories_groups,
        "jewelries_groups": jewelries_groups,
        "beauty_groups": beauty_groups,
        "main_nav_pic": main_nav_pic,
    }
    return context



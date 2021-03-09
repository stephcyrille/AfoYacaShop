import random

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings

from products.models import Product, Variety


def single_product(request, slug):
    template_name = 'products/single.html'
    product = get_object_or_404(Product, slug=slug)
    if product:
        varieties = list(Variety.objects.filter(product=product, is_archived=False))
        variety = random.choice(varieties)
        # varieties_number = len(varieties)
        # import pdb; pdb.set_trace()
        # TODO Get varieties number there, select specific variety randomly, then send it as context
    else:
        varieties = []
        variety = {}

    context = {
        "product": product,
        "varieties": varieties,
        "variety": variety,
    }
    return render(request, template_name, context)


def trending_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def clothing_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def children_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def shoes_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def bags_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def accessories_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def jewelries_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def beauty_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)


def to_wear_products(request):
    template_name = 'products/all.html'
    products = Product.objects.filter()

    context = {
        "products": products,
    }
    return render(request, template_name, context)

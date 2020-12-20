from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from products.models import Product


def single_product(request, slug):
    template_name = 'products/single.html'
    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product,
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

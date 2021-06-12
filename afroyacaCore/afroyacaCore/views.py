import random
from django.shortcuts import render

from editorial.models import Article
from products.models import Product, Category
from settings.models import Banner


def home(request):
    template_name = 'index.html'

    banner = Banner.objects.filter(is_home=True, is_published=True).first()
    cover = Article.objects.filter(is_home=True, is_published=True).first()
    trending_products = list(Product.objects.filter(is_archived=False, trending=True))
    if trending_products:
        feature_products = random.sample(trending_products, 2)
    else:
        feature_products = []
    categories_list = list(Category.objects.filter(is_archived=False))
    if categories_list:
        categories = random.sample(categories_list, 3)
    else:
        categories = []

    context = {
        "banner": banner,
        "cover": cover,
        "feature_products": feature_products,
        "categories": categories,
    }
    return render(request, template_name, context)

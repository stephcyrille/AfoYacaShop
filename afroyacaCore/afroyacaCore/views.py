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
    try:
        if trending_products:
            feature_products = random.sample(trending_products, 2)
        else:
            feature_products = []
    except Exception as e:
        feature_products = []
        print("Feature errrors", e.__str__())
    categories_list = list(Category.objects.filter(is_archived=False))
    try:
        if categories_list:
            categories = random.sample(categories_list, 3)
        else:
            categories = []
    except Exception as e:
        categories = []
        print("Categories errrors", e.__str__())

    context = {
        "banner": banner,
        "cover": cover,
        "feature_products": feature_products,
        "categories": categories,
    }
    return render(request, template_name, context)

import random
from django.shortcuts import render

from editorial.models import Article
from products.models import Product
from settings.models import Banner


def home(request):
    template_name = 'index.html'

    banner = Banner.objects.filter(is_home=True, is_published=True).first()
    cover = Article.objects.filter(is_home=True, is_published=True).first()
    trending_products = list(Product.objects.filter(is_archived=False))
    feature_products = random.sample(trending_products, 2)

    context = {
        "banner": banner,
        "cover": cover,
        "feature_products": feature_products,
    }
    return render(request, template_name, context)

from django.shortcuts import render

from products.models import Product
from settings.models import Banner


def home(request):
    template_name = 'index.html'

    banner = Banner.objects.filter(is_home=True, is_published=True).first()

    context = {}
    return render(request, template_name, context)

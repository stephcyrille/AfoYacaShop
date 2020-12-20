from django.contrib import admin
from .models import *

all_models = [
    Product,
    Variety,
    Group,
    Category,
    Catalog,
    Size,
    Color,
    Collection
]

for m in all_models:
    admin.site.register(m)

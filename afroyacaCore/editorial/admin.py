from django.contrib import admin
from .models import *

all_models = [
    Article
]

for m in all_models:
    admin.site.register(m)

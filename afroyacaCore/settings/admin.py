from django.contrib import admin
from .models import *

all_models = [
    MainMenuNavPicture,
    SeoPage,
    Banner,
]

for m in all_models:
    admin.site.register(m)


from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .apis import *


urlpatterns = [
    # Dashboard url
    path('my/orders', UserOrderAPIView.as_view(), name="user_orders_list"),
]

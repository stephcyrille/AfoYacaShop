from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('women/trending', views.trending_products, name="trending_products"),
    path('women/clothing', views.clothing_products, name="clothing_products"),
    path('children/clothing', views.children_products, name="children_products"),
    path('woman/shoes', views.shoes_products, name="shoes_products"),
    path('woman/bags', views.bags_products, name="bags_products"),
    path('woman/accessories', views.accessories_products, name="accessories_products"),
    path('woman/jewelries', views.jewelries_products, name="jewelries_products"),
    path('woman/beauty', views.beauty_products, name="beauty_products"),
    path('woman/to_wear', views.to_wear_products, name="to_wear_products"),
    path('women/single/<str:slug>', views.single_product, name="single_product"),
]

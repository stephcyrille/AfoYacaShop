from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.apis import *
from cart.apis import *
from mybox.apis import *

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/web/', include('account.urls')),
    path('shop/products/', include('products.urls')),
    path('shop/cart/', include('cart.urls')),
    path('shop/checkout/', include('checkout.urls')),
    path('magazine/', include('editorial.urls')),
    path('services/', include('services.urls')),
    path('', home, name="home"),
    path('api/list/products/flash_sales/', ProductFlashSaleAPIView.as_view(), name="product_flash_sales"),
    path('api/products/', AllProductsAPIView.as_view(), name='api_all_products'),
    path('api/products/<str:slug>/', ProductSingleAPIView.as_view(), name='api_single_product'),
    path('api/cart/add_item/', AddCartItemAPIView.as_view(), name='api_cart_add_item'),
    path('api/oh-my-box/my/', MyBoxAPIView.as_view(), name='api_my_box'),
    path('api/account/', include('account.api_url')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

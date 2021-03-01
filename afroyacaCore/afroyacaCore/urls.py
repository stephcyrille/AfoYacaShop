from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.apis import *

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/web/', include('account.urls')),
    path('shop/products/', include('products.urls')),
    path('shop/cart/', include('cart.urls')),
    path('shop/checkout/', include('checkout.urls')),
    path('magazine/', include('editorial.urls')),
    path('', home, name="home"),
    path('api/list/products/flash_sales/', ProductFlashSaleAPIView.as_view(), name="product_flash_sales"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

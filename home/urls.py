from django.urls import path
from home.views import index, productDetail, userCart
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('product/<product_id>/detail/', productDetail, name='productDetail'),
    path('product/cart/', userCart, name='productCart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
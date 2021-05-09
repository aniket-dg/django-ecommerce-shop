from django.urls import path
from home.views import index #, userCart, showCart, cartOperation, remove_product_from_cart
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    #path('product/cart/', userCart, name='productCart'),
    #path('user/cart/', showCart, name='showCart'),
    #path('user/cart/update/<productcart_id>/<op>', cartOperation, name='cartOpeartion'),
    #path('user/cart/<product_id>/remove/', remove_product_from_cart, name='remove_product_from_cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
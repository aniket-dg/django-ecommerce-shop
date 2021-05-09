from django.urls import path
from product.views import productDetail, remove_product_from_cart, cartOperation 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('view/<product_id>/detail.View/', productDetail, name='productDetail'),
    path('user/cart/update/<product_id>/delete/', remove_product_from_cart, name='remove_product_from_cart'),
    path('user/cart/update/<productcart_id>/<op>', cartOperation, name='cartOpeartion'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
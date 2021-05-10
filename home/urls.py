from django.urls import path
from home.views import index, listProduct, search_product
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('products/all/list.view', listProduct, name='listProduct'),
    path('search/product/', search_product, name='search_product'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
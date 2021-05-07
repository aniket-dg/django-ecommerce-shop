from django.urls import path
from home.views import index
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
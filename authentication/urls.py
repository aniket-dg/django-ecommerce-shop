from django.urls import path
from .views import userLogin
urlpatterns = [
    path('authenticate.do/', userLogin, name="userLogin"),
    path('', userLogin, name="userLogin"),
    
]
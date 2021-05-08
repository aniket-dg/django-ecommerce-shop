from django.urls import path
from .views import userLogin, userSignUp
urlpatterns = [
    path('authenticate.do/', userLogin, name="userLogin"),
    path('', userLogin, name="userLogin"),
    path('user/signup.do/', userSignUp, name="userSignUp"),
    
]
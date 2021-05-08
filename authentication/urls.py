from django.urls import path
from .views import userLogin, userSignUp, userLogout
urlpatterns = [
    path('authenticate.do/', userLogin, name="userLogin"),
    path('', userLogin, name="userLogin"),
    path('user/signup.do/', userSignUp, name="userSignUp"),
    path('user/logout/', userLogout, name="userLogout"),
    
]
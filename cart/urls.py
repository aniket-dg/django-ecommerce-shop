from django.urls import path
from cart.views import userCart, showCart, checkOutView
urlpatterns = [
    path('user/add/product/', userCart, name='userCart'),
    path('user/cart.view/', userCart, name='productCart'),
    path('user/cart.viewFull/', showCart, name='showCart'),
    path('user/checkout.view/', checkOutView, name='checkOutView'),
    
]
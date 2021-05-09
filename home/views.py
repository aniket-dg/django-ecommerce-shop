from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Shoes
from cart.views import extract_data_Cart, cleanCart

# Create your views here.
def index(request):
    context = {}
    cleanCart(request)
    context['Shoesdata'] = Shoes.objects.all()
    context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
    context['cart_total'] = len(context['product_list'])
    return render(request, 'index.html', context)
    

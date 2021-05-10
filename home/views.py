from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Shoes
from cart.views import extract_data_Cart, cleanCart
from shop.settings import HOST_MEDIA


# Create your views here.
def index(request):
    context = {}
    context['Shoesdata'] = Shoes.objects.all()[:8]
    if not request.user.is_anonymous:
        cleanCart(request)
        context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
        context['cart_total'] = len(context['product_list'])
    else:
       context['host_media'] = HOST_MEDIA
    return render(request, 'index.html', context)

def search_product(request):
    context = {}
    query = request.GET.get('q')
    context['is_search_data'] = True
    product_list = Shoes.objects.filter(name__icontains=query)
    if len(product_list) < 1:
        context['is_search_data'] = False
    context['Shoesdata'] = product_list
    if not request.user.is_anonymous:
        context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
        context['cart_total'] = len(context['product_list'])
    else:
        context['host_media'] = HOST_MEDIA
    return render(request, 'list_product.html', context)
    



def listProduct(request):
    context = {}
    data = Shoes.objects.all()
    context['is_search_data'] = True
    context['Shoesdata'] = data
    if not request.user.is_anonymous:
        context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
        context['cart_total'] = len(context['product_list'])
    else:
        context['host_media'] = HOST_MEDIA
    return render(request, 'list_product.html', context)

    

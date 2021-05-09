from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoes, ProductCart, Cart
from shop.settings import HOST_MEDIA
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    data = Shoes.objects.all()
    return render(request, 'index.html', { 'data':data , 'host_media':HOST_MEDIA })

@login_required(login_url = '/authentication/authenticate.do/')
def productDetail(request, product_id):
    try:
        product = Shoes.objects.get(id = int(product_id))
        return render(request, 'product-detail.html', { 'data': product, 'host_media': HOST_MEDIA })
    except ObjectDoesNotExist:
        return HttpResponse("404 Page not Found")

def userCart(request):
    if request.method == "POST":
        size, quantity, product_id = request.POST.get('size'), request.POST.get('quantity'), request.POST.get('product_id')
        product = Shoes.objects.get(id = product_id)
        user = User.objects.get(id = request.user.id)
        try:
            p_cart = ProductCart.objects.get(user_id = user, product_id = product, size = size)
        except ObjectDoesNotExist:
            p_cart = ProductCart(product_id = product, user_id = user, size = size)
        total = int(product.newPrice) * int(quantity)
        p_cart.quantity = quantity
        p_cart.total = total
        p_cart.save()
        updateCart(request, user)
        return redirect('/home/user/cart/')
    return render(request, 'user_cart.html')

def showCart(request):
    context = {}
    product_list = ProductCart.objects.filter(user_id = request.user)
    cart = Cart.objects.get(user_id = request.user)
    context['data'] = False
    context['host_media'] = HOST_MEDIA
    if len(product_list) > 0:
        context['product_list'] = product_list
        context['cart'] = cart
        context['data'] = True
    return render(request, 'user_cart.html', context)   

def updateCart(request, user): #Method for update User Cart
    products = ProductCart.objects.filter(user_id = user)
    total = 0
    if len(products) > 0:
        for data in products:
            total += data.total
    try:
        user_cart = Cart.objects.get(user_id = user)
    except ObjectDoesNotExist:
        user_cart = Cart(user_id = user)
    user_cart.cart_total = total
    user_cart.save()
    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Shoes, ProductCart, Cart
from shop.settings import HOST_MEDIA
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def index(request):
    context = {}
    cleanCart(request)
    context['Shoesdata'] = Shoes.objects.all()
    context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
    context['cart_total'] = len(context['product_list'])
    return render(request, 'index.html', context)

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

def updateProductCart(request, product_id): # update product cart using product_id
    user_product = ProductCart.objects.get(id = product_id)
    user_product.total = int(user_product.product_id.newPrice) * int(user_product.quantity)
    user_product.save()
    if user_product.quantity == 0:
        user_product.delete()

def showCart(request): 
    cleanProductCart(request)
    context = {}
    cleanCart(request)
    context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
    return render(request, 'user_cart.html', context) 

def extract_data_Cart(request): # Backend Method
    context = {}
    product_list = ProductCart.objects.filter(user_id = request.user)
    user_has_cart = True
    try:
        cart = Cart.objects.get(user_id = request.user)
    except ObjectDoesNotExist:
        cart = None
        user_has_cart = False
    data = False
    host_media = HOST_MEDIA
    if len(product_list) > 0:
        product_list = product_list
        cart = cart
        data = True
    return data, host_media, product_list, cart, user_has_cart 


def updateCart(request, user): #Method for update User Cart from userCart()
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

def cleanProductCart(request):
    products = ProductCart.objects.filter(user_id = request.user, quantity=0).delete()

def cleanCart(request):
    userCart = ProductCart.objects.filter(user_id = request.user)
    if len(userCart) == 0:
        Cart.objects.filter(user_id = request.user).delete()

    print("Cart Total:",len(userCart))
    
def cartOperation(request, productcart_id, op):
    change_item_to_cart(request, productcart_id, op)
    cleanProductCart(request)
    return redirect('/home/user/cart/')

def change_item_to_cart(request, productCart_id, op):
    product = ProductCart.objects.get(id = productCart_id)
    if op == "add":
        if product.quantity == 10:
            messages.warning(request,"Sorry Only 10 Quantities are allowed at one order")
        else:
            product.quantity += 1
    elif op == "remove":
        if product.quantity > 0:
            product.quantity -=1
    else:
        return HttpResponse("Bad Request")
    product.save()
    updateProductCart(request, product.id)
    updateCart(request, request.user)

def remove_product_from_cart(request, product_id):
    product = ProductCart.objects.filter(id = product_id).delete()
    return redirect('/home/user/cart/')
    

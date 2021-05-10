from django.shortcuts import render, redirect
from cart.models import Cart
from product.models import ProductCart, Shoes
from django.contrib.auth.models import User
from shop.settings import HOST_MEDIA
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse
from billing.models import Billing, Address
from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = '/authentication/authenticate.do/')
def userCart(request): # Method for adding product to your Cart
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
        return redirect('/cart/user/cart.viewFull/')
    return render(request, 'user_cart.html')

@login_required(login_url = '/authentication/authenticate.do/')
def showCart(request): 
    cleanProductCart(request)
    context = {}
    cleanCart(request)
    context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
    context['cart_total'] = len(context['product_list'])
    return render(request, 'user_cart.html', context) 

@login_required(login_url = '/authentication/authenticate.do/')
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

@login_required(login_url = '/authentication/authenticate.do/')
def updateCart(request, user): #Method for update User Cart from userCart()
    products = ProductCart.objects.filter(user_id = user)
    total = 0
    product_list = []
    if len(products) > 0:
        for data in products:
            total += data.total
            product_list.append(data.id)
    try:
        user_cart = Cart.objects.get(user_id = user)
    except ObjectDoesNotExist:
        user_cart = Cart(user_id = user)
    user_cart.cart_total = total
    user_cart.products_list = json.dumps(product_list)
    user_cart.save()

@login_required(login_url = '/authentication/authenticate.do/')
def cleanCart(request):
    userCart = ProductCart.objects.filter(user_id = request.user)
    if len(userCart) == 0:
        Cart.objects.filter(user_id = request.user).delete()

@login_required(login_url = '/authentication/authenticate.do/')
def cleanProductCart(request):
    products = ProductCart.objects.filter(user_id = request.user, quantity=0).delete()

@login_required(login_url = '/authentication/authenticate.do/')
def clean_Cart_after_orderPlaced(request):
    cart = ProductCart.objects.filter(user_id = request.user).delete()
    f_cart = Cart.objects.filter(user_id = request.user).delete()
    cleanCart(request)
    cleanProductCart(request)

@login_required(login_url = '/authentication/authenticate.do/')
def checkOutView(request):
    if request.method == "POST":
        cart_id = Cart.objects.get(user_id = request.user)
        address_id = Address.objects.get(user_id = request.user)
        card_number = request.POST['card_number']
        cvv = request.POST['cvv']
        ordered_data = date.today()
        delivery_data = date.today() + timedelta(2)
        extra_stuff_notes = request.POST['order_notes']
        total = cart_id.cart_total
        bill = Billing(cart_id = cart_id, address_id = address_id, card_number = card_number, cvv = cvv, ordered_data = ordered_data, delivery_data = delivery_data, extra_stuff_notes = extra_stuff_notes, total = total)
        bill.save()
        clean_Cart_after_orderPlaced(request)
        success_msg = "Order Placed Successfully. Expected Delivery on {date}".format(date = delivery_data)
        messages.success(request, success_msg)
        return redirect('/home')
    else:
        try:
            cart = Cart.objects.get(user_id = request.user)
            user_add = Address.objects.get(user_id = request.user)
            product_list = json.loads(cart.products_list)
            products = []
            for id in product_list:
                products.append(ProductCart.objects.get(id = id))
            return render(request, 'cart/checkout.html', { 'cart':cart, 'products':products, 'user_add': user_add })
        except ObjectDoesNotExist:
            return HttpResponse("Sorry your Cart not Found")


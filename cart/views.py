from django.shortcuts import render, redirect
from cart.models import Cart
from product.models import ProductCart, Shoes
from django.contrib.auth.models import User
from shop.settings import HOST_MEDIA
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
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

def showCart(request): 
    cleanProductCart(request)
    context = {}
    cleanCart(request)
    context['data'], context['host_media'], context['product_list'], context['cart'], context['user_has_cart'] = extract_data_Cart(request)
    context['cart_total'] = len(context['product_list'])
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

def cleanCart(request):
    userCart = ProductCart.objects.filter(user_id = request.user)
    if len(userCart) == 0:
        Cart.objects.filter(user_id = request.user).delete()

    print("Cart Total:",len(userCart))

def cleanProductCart(request):
    products = ProductCart.objects.filter(user_id = request.user, quantity=0).delete()

from django.shortcuts import render, redirect
from product.models import Shoes, ProductCart
from cart.views import updateCart, cleanProductCart
from django.core.exceptions import ObjectDoesNotExist
from shop.settings import HOST_MEDIA
# Create your views here.
def productDetail(request, product_id):
    try:
        product = Shoes.objects.get(id = int(product_id))
        return render(request, 'product-detail.html', { 'data': product, 'host_media': HOST_MEDIA })
    except ObjectDoesNotExist:
        return HttpResponse("404 Page not Found")
    
def updateProductCart(request, product_id): # update product cart using product_id
    user_product = ProductCart.objects.get(id = product_id)
    user_product.total = int(user_product.product_id.newPrice) * int(user_product.quantity)
    user_product.save()
    if user_product.quantity == 0:
        user_product.delete()



def cartOperation(request, productcart_id, op):
    change_item_to_cart(request, productcart_id, op)
    cleanProductCart(request)
    return redirect('/cart/user/cart.viewFull/')

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
    return redirect('/cart/user/cart.viewFull/')

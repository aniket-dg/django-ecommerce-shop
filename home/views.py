from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoes
from shop.settings import HOST
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    data = Shoes.objects.all()
    return render(request, 'index.html', { 'data':data , 'host':HOST })

def productDetail(request, product_id):
    try:
        product = Shoes.objects.get(id = int(product_id))
        return render(request, 'product-detail.html', { 'data': product })
    except ObjectDoesNotExist:
        return HttpResponse("404 Page not Found")
    
from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoes
from shop.settings import HOST
# Create your views here.
def index(request):
    data = Shoes.objects.all()
    return render(request, 'index.html', { 'data':data , 'host':HOST })

def productDetail(request):
    return render(request, 'product-detail.html')
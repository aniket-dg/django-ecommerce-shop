from django.db import models
from django.contrib.auth.models import User
class Shoes(models.Model):
    name = models.CharField(max_length=30)
    shoes_category = (
        ('nike', 'Nike'),
        ('adidas','Adidas'),
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids')
    )
    category = models.CharField(max_length=10, choices=shoes_category)
    desc = models.CharField(max_length=30)
    isNew = models.BooleanField()
    isInOffer = models.BooleanField()
    discount = models.CharField(max_length=10)
    oldPrice = models.IntegerField(default=0)
    newPrice = models.IntegerField(default=0)
    img = models.ImageField(upload_to='media/')
    isInTopSale = models.BooleanField(default=False)
    extraStuff = models.TextField(primary_key=False)

class ProductCart(models.Model):
    product_id = models.OneToOneField(Shoes, on_delete=models.CASCADE)
    quantity = models.IntegerField(primary_key=False, default=0)
    total = models.IntegerField(primary_key=False, default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    productCart_id = models.OneToOneField(ProductCart, on_delete=models.CASCADE)
    cart_total = models.IntegerField(primary_key=False, default=0)
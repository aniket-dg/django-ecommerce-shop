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

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class ProductCart(models.Model):
    product_id = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.IntegerField(primary_key=False, default=0)
    total = models.IntegerField(primary_key=False, default=0)
    size = models.CharField(max_length=5, default=4)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['product_id']

class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_total = models.IntegerField(primary_key=False, default=0)
    
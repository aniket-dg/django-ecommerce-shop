from django.db import models

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
    oldPrice = models.CharField(max_length=20)
    newPrice = models.CharField(max_length=20)
    img = models.ImageField(upload_to='media/')
    isInTopSale = models.BooleanField(default=False)
    extraStuff = models.TextField(primary_key=False)
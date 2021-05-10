from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Billing(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    ordered_data = models.DateField()
    delivery_data = models.DateField()
    extra_stuff_notes = models.TextField(default="")
    total = models.CharField(max_length=5)
from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    products_list = models.JSONField()
    cart_total = models.IntegerField(primary_key=False, default=0)
    is_order_placed = models.BooleanField(default=False)
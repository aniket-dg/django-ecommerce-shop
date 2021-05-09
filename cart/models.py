from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_total = models.IntegerField(primary_key=False, default=0)
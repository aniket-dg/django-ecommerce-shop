from django.contrib import admin
from cart.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'cart_total')
    list_filter = ('user_id',)

admin.site.register(Cart, CartAdmin)
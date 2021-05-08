from django.contrib import admin
from home.models import Shoes, ProductCart, Cart
# Register your models here.

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'oldPrice', 'newPrice')

class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'user_id', 'quantity', 'total')
    list_filter =  ('user_id',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('productCart_id', 'cart_total')

admin.site.register(Shoes, ShoesAdmin)
admin.site.register(ProductCart, ProductCartAdmin)
admin.site.register(Cart, CartAdmin)


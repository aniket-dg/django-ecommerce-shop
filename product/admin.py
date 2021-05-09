from django.contrib import admin
from product.models import Shoes, ProductCart
# Register your models here.
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'oldPrice', 'newPrice')
admin.site.register(Shoes, ShoesAdmin)

class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'user_id', 'quantity', 'size', 'total')
    list_filter =  ('user_id','product_id', 'size')

admin.site.register(ProductCart, ProductCartAdmin)


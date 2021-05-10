from django.contrib import admin
from billing.models import Billing, Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id' ,'user_id', 'address')

class BillingAdmin(admin.ModelAdmin):
    list_display = ('id','address_id', 'cart_id', 'total')


admin.site.register(Billing, BillingAdmin)
admin.site.register(Address, AddressAdmin)
from django.contrib import admin

# Register your models here.
from .models import Orders, Product, Contact, OrderUpdate, Profile

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Profile)

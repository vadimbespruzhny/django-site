from django.contrib import admin
# from my_first_site.note.models import Notebook
# Register your models here.
from .models import Product, OrderItem, Order


class OrderAdmin(admin.ModelAdmin): 
    list_display = ['id', 'user', 'ordered']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'item', 'quantity']


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)

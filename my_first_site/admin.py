from django.contrib import admin
from my_first_site.note.models import Product, Description, New_model
from django.contrib.auth.models import User


class New_modelAdmin(admin.ModelAdmin):
    model = New_model

admin.site.register(New_model, New_modelAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product

admin.site.register(Product, ProductAdmin)


class ProductItemInline(admin.TabularInline):
    model = Product
    list_display = ['name', 'color']


class DescriptionAdmin(admin.ModelAdmin):
    model = Description


admin.site.register(Description, DescriptionAdmin)

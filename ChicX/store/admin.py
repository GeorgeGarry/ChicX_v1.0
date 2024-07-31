from django.contrib import admin

# Register your models here.
from .models import *

# class ProductSizeInline(admin.TabularInline):
#     model = ProductSize
#     extra = 1
#
#
# class ProductColorInline(admin.TabularInline):
#     model = ProductColor
#     extra = 1
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price']
#     inlines = [ProductSizeInline, ProductColorInline]

admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Size)
admin.site.register(Color)

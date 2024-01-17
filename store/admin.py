from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
admin.site.register(Product, ProductAdmin)
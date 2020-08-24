from .models import User, Product
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)

admin.site.register(User)


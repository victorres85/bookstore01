from django.contrib import admin

# Register your models here.
from .models import Product, Category, Wine


admin.site.register(Product)

from django.contrib import admin

from app.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price','description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin )
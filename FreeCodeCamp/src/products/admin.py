from django.contrib import admin

# Add relative import of models
from .models import Product

# Register your models here.
admin.site.register(Product)

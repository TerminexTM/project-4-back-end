from django.contrib import admin
# Register your models here.
from .models import Product
from .models import Company

admin.site.register(Product)
admin.site.register(Company)

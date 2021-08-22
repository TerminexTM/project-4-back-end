from django.contrib import admin
# Register your models here.
from .models import Product
from .models import Company
from .models import UserAccount

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(UserAccount)

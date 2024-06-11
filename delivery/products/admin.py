from django.contrib import admin
from .models import Product, Users

admin.site.register([Product, Users])

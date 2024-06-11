from django.shortcuts import render
from .models import Users, Product
from django.views import View


class UserView(View):
    def get(self, request):
        users = Users.objects.all()
        return render(request, "users.html", {"users": users})


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "product.html", {"products": products})

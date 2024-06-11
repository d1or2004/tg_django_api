from django.urls import path
from .views import UserView, ProductsView

urlpatterns = [
    path("", UserView.as_view(), name="users"),
    path("product/", ProductsView.as_view(), name="product")
]

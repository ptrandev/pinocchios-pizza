from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("shopping_cart", views.shopping_cart, name="shopping_cart"),
    path("shopping_cart_items", views.shopping_cart_items,
         name="shopping_cart_items"),
    path("add_item_to_cart", views.add_item_to_cart,
         name="add_item_to_cart"),
    path("remove_item_from_cart", views.remove_item_from_cart,
         name="remove_item_from_cart"),
    path("customize_pizza", views.customize_pizza, name="customize_pizza"),
    path("add_pizza_to_cart", views.add_pizza_to_cart, name="add_pizza_to_cart"),
    path("customize_sub", views.customize_sub, name="customize_sub"),
    path("add_sub_to_cart", views.add_sub_to_cart, name="add_sub_to_cart"),
]

from django.contrib import admin
from django.urls import path
from giftshopapp import views

urlpatterns = [
    path("", views.signUp, name='signUp'),
    path("signUp", views.signUp, name='signUp'),
    path("login", views.login, name='login'),
    path("main",views.main,name='main'),
    path("menu", views.menu, name='menu'),
    path("personalized", views.personalized, name='personalized'),
    path("cakes", views.cakes, name='cakes'),
    path("co_gifts", views.co_gifts, name='co_gifts'),
    path("flower", views.flower, name='flower'),
    path("gourmet", views.gourmet, name='gourmet'),
    path("new_arrivals",views.new_arrivals,name='new_arrivals'),
    path("plant",views.plant,name='plant'),
    path("wishlist",views.wishlist,name='wishlist'),
    path("cart",views.cart,name='cart'),
    path("profile",views.profile,name='profile')
]

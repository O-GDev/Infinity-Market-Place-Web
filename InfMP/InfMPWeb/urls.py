from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sellerlogin/', views.sellerlogin, name="sellerlogin"),
    path('buyerlogin/', views.buyerlogin, name="buyerlogin"),
    path('sellersignup/', views.register_seller, name="sellersignup"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('help/', views.help, name="help"),
    path('pricing/', views.pricing, name="pricing"),
    path('buyersignup/', views.register_buyer, name="buyersignup"),
]
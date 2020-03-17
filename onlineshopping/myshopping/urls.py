from django.contrib import admin
from django.urls import path
from myshopping import views
from . import views
from cart.views import CartView, add_to_cart, remove_from_cart
app_name= 'mainapp'

urlpatterns=[
    # ex: /library/
    # path('', views.index, name='index'),
    path('', views.product_list, name='list'),
    path('cart/<product_id>', add_to_cart, name='cart'),
    path('remove/<product_id>', remove_from_cart, name='remove-cart'),
    path('cartview/', CartView, name='cart-home'),
]
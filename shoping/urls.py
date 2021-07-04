from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop_main', views.shop_main, name='shop_main'),
    path('shop/', views.shop, name='shop'),
    path('shop_right_sidebar', views.shop_right_sidebar, name='shop_right_sidebar'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('error', views.error, name='error'),
    path('login', views.handlelogin, name='login'),
    path('register', views.register, name='register'),
    path('no_data_found', views.no_data_found, name='no_data_found'),
    path('place_order', views.place_order, name='place_order'),
    path('order_tracking', views.order_tracking, name='order_tracking'),
    path('order_transaction', views.order_transaction, name='order_transaction'),
    path('place_order', views.place_order, name='place_order'),
    path('product_detail', views.product_detail, name='product_detail'),
    path('profile_detail', views.profile_detail, name='profile_detail'),
    path('terms_and_condition', views.terms_and_condition, name='terms_and_condition'),
    path('thank_you', views.thank_you, name='thank_you'),
    path('wishlist', views.wishlist, name='wishlist'),
]


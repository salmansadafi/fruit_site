from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('404/',notfound_view, name='404'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('shop/', shop_view, name='shop'),
    path('single-product/<int:pid>', single_product_view, name='single_product'),
    path('category/<str:category>', index_view, name='category'),
    path('subscribe/', subscribe_view, name='subscribe'),
    
]
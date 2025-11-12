from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('my-orders/', views.my_orders, name='my_orders'),
    #path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my-orders/', views.my_orders, name='my_orders'),
    #path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('confirm-cod/<int:order_id>/', views.confirm_cod, name='confirm_cod'),
    path('pay-now/<int:order_id>/', views.pay_now, name='pay_now'),
    path('confirm-payment/<int:order_id>/', views.confirm_payment, name='confirm_payment'),


]

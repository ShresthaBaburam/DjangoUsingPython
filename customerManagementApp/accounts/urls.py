from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('customer/<str:pk_test>',views.customer, name="customer"),
    path('products/',views.product, name="product"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('user/',views.userPage, name="user"),

    path('account/',views.accountSettings, name="account"),

    
]

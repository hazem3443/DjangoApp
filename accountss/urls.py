from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage,name='registerPage'),
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutUser,name='logout'),
    path('user_settings/', views.user_settings,name='account'),


    path('', views.home,name='home'),
    path('user/', views.userPage,name='user-page'),
    path('products/', views.products,name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),
 
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pku>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pkd>', views.deleteOrder, name='delete_order'),

    path('create_order/<str:pkm>', views.createMultipleOrder, name='create_multiple_order'),
]
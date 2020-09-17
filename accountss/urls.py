from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('register/', views.registerPage,name='registerPage'),
    path('login/', views.loginPage,name='loginPage'),
    path('logout/', views.logoutUser,name='logout'),
    path('user_settings/', views.user_settings,name='account'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="accountss/password_reset.html"), name = "password_reset"),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accountss/password_reset_sent.html"), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accountss/password_reset_confirm.html"), name = "password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accountss/password_reset_done.html"), name = "password_reset_complete"),

    path('', views.home,name='home'),
    path('user/', views.userPage,name='user-page'),
    path('products/', views.products,name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),
 
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pku>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pkd>', views.deleteOrder, name='delete_order'),

    path('create_order/<str:pkm>', views.createMultipleOrder, name='create_multiple_order'),
]
from django.urls import path

from apps.views import home, daily_sell, stock, user_login, user_logout, clear

urlpatterns = [

    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('',home,name='home'),
    path('home/',home,name='home'),
    path('daily_sell/',daily_sell,name='daily_sell'),
    path('stock/',stock,name='stock'),
    path('clear/',clear,name='clear'),

]
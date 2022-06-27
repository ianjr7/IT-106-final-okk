from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_home, name="login_home"),
    path('accounts/google/login/callback/home/', views.home, name="home"),
    path('logout/', views.logout_user, name="logout")
   
]

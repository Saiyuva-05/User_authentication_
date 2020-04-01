from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('register/', views.registeruser, name='registeruser'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logoutuser, name='logoutuser'),

]

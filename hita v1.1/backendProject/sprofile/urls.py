from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_view #for login and logout

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),

    path('thankyou/', views.thankyou, name='thankyou'),
    path('thankyouuu/', views.thankyouuu, name='thankyouuu'),
    path('login/', auth_view.LoginView.as_view(template_name='sprofile/login.html'), name='login'),
    path('profile/logout/', auth_view.LogoutView.as_view(template_name='sprofile/logout.html'), name='logout'),
    path('sell/', views.sell, name='sell'),
    path('will/', views.will, name='will'),
    path('lease/', views.lease, name='lease'),
    path('signup/', views.signup, name='signup'),
    path('sellform/', views.sellform, name='sellform'),
    path('accounts/', include('allauth.urls')),

]

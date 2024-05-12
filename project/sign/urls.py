from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, ConfirmUser, ProfileViev

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='signup.html'),
         name='signup'),

    path('inactive/', ConfirmUser.as_view(), name='confirm_user'),

    path('profile/', ProfileViev.as_view(), name='profile'),

]
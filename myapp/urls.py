from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# write your urls here

urlpatterns = [
    path('', views.index, name='index'),

    #login
    path('login/', views.LoginView, name='login'),

    #logout
    path('logout/', views.LogoutView, name='logout'),

    #profile
    path('profile/<int:id>', views.Profile, name='profile'),

    #password
    path('change_password_form/<int:id>', views.ChangePasswordForm, name='change_password_form'),
    path('change_password/<int:id>', views.ChangePassword, name='change_password'),
    path('password_confirmation/<int:id>', views.PasswordConfirmation, name='password_confirmation'),


] 
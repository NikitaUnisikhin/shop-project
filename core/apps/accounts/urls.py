from django.urls import path
from . import views

urlpatterns = [
    path('accounts/users/', views.users),
    path('accounts/register/', views.register),
    path('accounts/login/', views.login),
    path('accounts/profile/', views.profile)
]

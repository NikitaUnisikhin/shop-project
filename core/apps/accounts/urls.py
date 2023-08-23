from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.users),
    path('api/register/', views.register),
    path('api/login/', views.login),
    path('api/profile/', views.profile)
]

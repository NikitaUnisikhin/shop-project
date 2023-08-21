from django.urls import path
from django.contrib.auth import views as views_auth
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views_auth.LoginView.as_view(template_name='login.html'))
]

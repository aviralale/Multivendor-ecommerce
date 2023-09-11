from django.contrib import admin
from django.urls import path, include
from .views import index, contact, signup
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('signup/', signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='auth/login.html',authentication_form =LoginForm), name='login')
]

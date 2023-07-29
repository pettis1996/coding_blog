from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name="registration/change-password.html"), name="password_change"),
    path('password_success/', PasswordsChangeView.as_view(template_name="registration/password_success.html"), name="password_success"),
]

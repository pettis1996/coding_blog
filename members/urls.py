from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditUserProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name="registration/change-password.html"), name="password_change"),
    path('password_success/', PasswordsChangeView.as_view(template_name="registration/password_success.html"), name="password_success"),
    path('<int:pk>/user_profile/', ShowProfilePageView.as_view(template_name="registration/user_profile.html"), name="user_profile"),
    path('<int:pk>/edit_user_profile/', EditUserProfileView.as_view(template_name="registration/edit_user_profile.html"), name="edit_user_profile"),
]

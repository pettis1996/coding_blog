from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from main_blog.models import Profile

class EditUserProfileForm(forms.ModelForm):
    website_url = forms.CharField(max_length=255, widget = forms.TextInput(attrs={'class': 'form-control'}))
    github_url = forms.CharField(max_length=255, widget = forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(max_length=255, widget = forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_url = forms.CharField(max_length=255, widget = forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'github_url', 'instagram_url', 'linkedin_url')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=20, widget = forms.TextInput(attrs={'class': 'form-control', "disabled": ""}))
    last_login = forms.CharField(max_length=50, widget = forms.DateTimeInput(attrs={'class': 'form-control', "disabled": ""}))
    is_active = forms.CharField(max_length=20, widget = forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'last_login', 'is_active')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['class'] = 'invisible'
        self.fields['password'].help_text = "Password is Hidden. Click on the <b>'Change Password'</b> Button to change your current password"

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=150, label="Old Password", widget = forms.PasswordInput(attrs={'class': 'form-control', "type": "password"}))
    new_password1 = forms.CharField(max_length=150, label="New Password", widget = forms.PasswordInput(attrs={'class': 'form-control', "type": "password"}))
    new_password2 = forms.CharField(max_length=150, label="New Password Confirmation", widget = forms.PasswordInput(attrs={'class': 'form-control', "type": "password"}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
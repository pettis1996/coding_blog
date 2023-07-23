from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')     # reverse_lazy is used to redirect to the login page after registration

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')     # reverse_lazy is used to redirect to the login page after registration

    def get_object(self):
        return self.request.user
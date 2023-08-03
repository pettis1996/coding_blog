from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from main_blog.models import Profile
from .forms import EditUserProfileForm, PasswordChangingForm, SignUpForm, EditProfileForm

class EditUserProfileView(generic.UpdateView):
    model = Profile 
    form_class = EditUserProfileForm
    template_name = "registration/edit_user_profile.html"
    success_url = reverse_lazy('home')

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)   

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "registration/password_success.html", {})

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
from django.shortcuts import render
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from . import forms

# Create your views here.

# redirect the user when they are logging out of the account
class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self,request, *args, **kwargs):
        logout(request)
        return super().get(request, *args,**kwargs) ## gets its normal return

## signup view for the viewer to sign up
class SignUp(generic.CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
                        UserCreationForm,
                        UserChangeForm,
                     PasswordChangeForm)
from django.contrib.auth.models import  User
from accounts.forms import SignupForm, EditProfileForm


# Create your views here.

## sign up view for the user to sign up
def register(request):
    if request.method =='POST':
            form  = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')
            else:
                        print("did not work")
                        form = SignupForm()
                        args = {'form':form}
                        return render(request,'accounts/signup.html',args)
    else:
            form = SignupForm()
            args = {'form':form}
            return render(request,'accounts/signup.html',args)
# profile view for the user and friends of user to see thier profile


@login_required
def view_profile(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request,'accounts/profile.html',args)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
                        form.save()
                        return redirect('accounts/profile')
        else:
                form = EditProfileForm(instance = request.user)
                args = {'form': form}
                return render(request,'accounts/edit_profile.html',args)
# could be error here in the future
    else:
            form = EditProfileForm(instance = request.user)
            args = {'form': form}
            return render(request,'accounts/edit_profile.html',args)

# lets the user change thier password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
                        form.save()
                        update_session_auth_hash(request,form.user)
                        return redirect('accounts/profile')
        else:
                return redirect(reverse('accounts:change_password'))
# could be error here in the future
    else:
            form = PasswordChangeForm(user= request.user)
            args = {'form': form}
            return render(request,'accounts/change_password.html',args)

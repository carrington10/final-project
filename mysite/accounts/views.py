from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import (
                        UserCreationForm,
                        UserChangeForm,
                     PasswordChangeForm)
from django.contrib.auth.models import  User
from accounts.forms import SignupForm, EditProfileForm
from animeweb.models import Friend, Wallpost
from animeweb.forms import WallForm
from django.views.generic.edit import CreateView


# Create your views here.
'''
 A view function that allows the users to signup and create an account
'''

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
'''
view function that allow the usr to view thier own profile, or other users profiles
'''

@login_required
def view_profile(request,pk=None):
    if pk:

            user = User.objects.get(pk=pk)

            try:
                    friend = Friend.objects.get(current_user=user)
                    friends = friend.users.all()

            except Friend.DoesNotExist:
                            friends = None;
            try:
                  wallp = Wallpost.objects.filter(to_user = user)
            except Wallpost.DoesNotExist:
                              wallp = None;

    else:

        user = request.user
        wallp = Wallpost.objects.filter(to_user=request.user)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    args = {'user': user,'friends':friends, 'wallps':wallp}
    return render(request,'accounts/profile.html',args)

'''
function to that allows users to edit and change thier profile information
'''
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user.userprofile)
        if form.is_valid():
                        form.save()
                        return redirect(reverse('accounts:view_profile'))
        else:
                form = EditProfileForm(instance = request.user.userprofile)
                args = {'form': form}
                return render(request,'accounts/edit_profile.html',args)
# could be error here in the future
    else:
            form = EditProfileForm(instance = request.user.userprofile)
            args = {'form': form}
            return render(request,'accounts/edit_profile.html',args)

'''
function that lets the users change thier password
'''
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
'''
class based view that allows thr users to post on other users wall
'''
class WallView(LoginRequiredMixin,CreateView):
        def get(self, request, pk):
            form = WallForm()
            return render(request, 'accounts/add_wall.html', {'form':form})
        def post(self, request, pk):
            form = WallForm(request.POST)
            if form.is_valid():
                wall = form.cleaned_data.get("wall")
                to_user = User.objects.get(pk=int(pk))
                wall_post = Wallpost(wall=wall, to_user=to_user, user=request.user)
                wall_post.save()
                return redirect('accounts:view_profilepk',pk = to_user.pk)
            return render(request, self.template_name, {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm

# Create your views here.

## sign up view for the user to sign up
def register(request):
    if request.method =='POST':
            form  = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts')
            else:
                        print("did not work")
                        form = SignupForm()
                        args = {'form':form}
                        return render(request,'accounts/signup.html',args)
    else:
            form = SignupForm()
            args = {'form':form}
            return render(request,'accounts/signup.html',args)

from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserProfile
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import HomeForm
from .models import Friend, Post

# Create your views here.



class HomeView(TemplateView):
    template_name = 'vanta/home.html'
    def get(self,request):
                    form = HomeForm()
                    posts = Post.objects.all().order_by('-created')
                    users = User.objects.exclude(id=request.user.id)
                    friend = Friend.objects.get(current_user=request.user)
                    friends = friend.users.all()
                    args = {
                            'form': form, 'posts': posts, 'users': users, 'friends': friends
                        }
                    return render(request, self.template_name, args)
    def post(self,request):
        form =  HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user =request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('animeweb:home')
        args = {'form':form,'text':text}
        return render(request, self.template_name, args)




@login_required
def change_friends(request,operation,pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user,friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user,friend)
    return redirect('animeweb:home')

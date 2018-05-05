from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserProfile
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HomeForm, CommentForm
from .models import Friend, Post, Comment

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



class PostView(TemplateView):
      template_name = 'vanta/video_detail.html'
      def get(self,request,pk):
          post = Post.objects.get(pk=pk)
          videofile= post.video
          args = {'post': post}
          return render(request, self.template_name,args)

class CommentView(LoginRequiredMixin,CreateView):
      template_name = 'vanta/add_comment.html'
      model = Comment
      form_class = CommentForm
      def post(self,request,pk):
                 post = get_object_or_404(Post, pk=pk)
                 if request.method == "POST":
                        form = CommentForm(request.POST)
                        if form.is_valid():
                            comment = form.save(commit=False)
                            comment.post = post
                            comment.save()
                            return redirect('animeweb:post_view', pk=post.pk)
                 else:
                            form = CommentForm()
                            return render(request, self.template_name, {'form': form})



@login_required
def change_friends(request,operation,pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user,friend)
        Friend.make_friend(friend,request.user)
    elif operation == 'remove':
        Friend.lose_friend(request.user,friend)
        Friend.lose_friend(friend,request.user)

    return redirect('animeweb:home')

from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserProfile
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HomeForm, CommentForm
from .models import Friend, Post, Comment, Rating

# Create your views here.temp


'''
class view that displays the homepage of the user
The get function returns a link to the videos , and current friends of the users
The post functons lets the user create a new video, and post it on the slideshow
'''
class HomeView(TemplateView):
    template_name = 'vanta/home.html'
    def get(self,request):
                    form = HomeForm()
                    posts = Post.objects.all().order_by('-created')
                    users = User.objects.exclude(id=request.user.id)
                    try:
                            friend = Friend.objects.get(current_user=request.user)
                            friends = friend.users.all()

                    except Friend.DoesNotExist:
                                    friends = None;
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


'''
Post view for displaying  the current video and getting thier Post objects related to the video clicked
'''
class PostView(TemplateView):
      template_name = 'vanta/video_detail.html'
      def get(self,request,pk):
          post = Post.objects.get(pk=pk)
          videofile= post.video
          args = {'post': post}
          return render(request, self.template_name,args)


'''
This view class is for the user to create and post comments on the video they are currently on
also displays
 '''
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
                            comment.creator = request.user
                            comment.save()
                            return redirect('animeweb:post_view', pk=post.pk)
                 else:
                            form = CommentForm()
                            return render(request, self.template_name, {'form': form})

'''
class based view to allow users to make video posts
'''
class NewVideoView(LoginRequiredMixin,CreateView):
        template_name = 'vanta/add_video.html'
        model = Post
        form_class = HomeForm
        def post(self,request):
            form =  HomeForm(request.POST,request.FILES)
            print("hello")
            if form.is_valid():
                title = form.cleaned_data.get("title")
                description = form.cleaned_data.get("description")
                video = form.cleaned_data.get("video")
                image = form.cleaned_data.get("image")
                videop = Post(title=title,description=description,user=request.user,image=image,video=video)
                videop.save()
                return redirect('animeweb:home')
            args = {'form':form}
            return render(request, self.template_name, args)


'''
class based views for rating users videos
'''

class RatingView(LoginRequiredMixin,TemplateView):
    def post(self,request):
        videoid= request.POST.get("videoId")
        counted = request.Post.get("count")
        video= Post.object.get( id= videoid )
        ratings,created=  Rating.objects.get_or_create(user= request.user,rating =video)
        ratings.count= counted
        ratings.save()
        total_videos = Rating.objects.filter(rating = video).values_list("count",flat=True)
        average = avg(total_videos)
        resonse["average"]=int(average)
        return HttpResponse(json.dump(response),status=201)

'''
function that lets the user add and remove friends
'''
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

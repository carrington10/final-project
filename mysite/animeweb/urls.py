from django.conf.urls import url
from animeweb.views import HomeView, PostView, CommentView, RatingView, NewVideoView
from . import views
from django.contrib.auth.views import login
import json

'''
Urls for routing users videos posts, and adding and removing friends
'''
app_name="animeweb"
urlpatterns =[
url(r'^$',HomeView.as_view(), name = 'home'),
url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
url(r'^video/(?P<pk>\d+)/$',PostView.as_view(), name = 'post_view'),
url(r'^video/(?P<pk>\d+)/comment/$', CommentView.as_view(), name='add_comment'),
url(r'^home/$',NewVideoView.as_view(), name = 'new_video'),
url(r'^video/(?P<pk>\d+)/$',RatingView.as_view(), name = 'post_rating'),
##url(r'login/$',login,{'template_name':'vanta/login.html'})

]

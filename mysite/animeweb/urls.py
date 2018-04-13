from django.conf.urls import url
from animeweb.views import HomeView
from . import views
from django.contrib.auth.views import login


app_name="animeweb"
urlpatterns =[
url(r'^$',HomeView.as_view(), name = 'home'),
   url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
##url(r'login/$',login,{'template_name':'vanta/login.html'})

]

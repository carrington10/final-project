from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


app_name="animeweb"
urlpatterns =[
url(r'home/$',views.home, name = 'home'),
##url(r'login/$',login,{'template_name':'vanta/login.html'})

]

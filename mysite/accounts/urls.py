from django.conf.urls import url
from . import views
from django.contrib.auth.views import login ,logout


app_name = 'accounts';
urlpatterns = [
# url(r"login/$", views.Loginview.as_view(),name="login")
url(r"^login/$",login,{'template_name':'accounts/login.html'}),
url(r"^logout/$",logout,{'template_name': 'accounts/logout.html'}),
url(r'^register',views.register, name = 'register')

]

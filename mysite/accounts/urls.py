from django.conf.urls import url
from . import views
from django.contrib.auth.views import login ,logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from accounts.views import WallView

'''
urls that links to varous methods that involves handling and creating users accounts 
'''
app_name = 'accounts';
urlpatterns = [
# url(r"login/$", views.Loginview.as_view(),name="login")
url(r"^login/$",login,{'template_name':'accounts/login.html'}),
url(r"^logout/$",logout,{'template_name': 'accounts/logout.html'}),
url(r'^register',views.register, name = 'register'),
url(r'^profile/$',views.view_profile, name = 'view_profile'),
url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profilepk'),
url(r'^profile/edit$',views.edit_profile, name = 'edit_profile'),
url(r'^profile/passwordchange$',views.change_password, name = 'change_password'),
url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),
url(r'^reset-password/done/$',password_reset_done,{'template_name':'accounts/password_reset_done.html'},name = 'password_reset_done'),
url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
url(r'^reset-password/complete/$',password_reset_confirm,{'template':'accounts/password_reset_complete.html'},name = 'password_reset_complete'),
url(r'^profile/(?P<pk>\d+)/wallpost/$', WallView.as_view(), name='add_wall'),
]

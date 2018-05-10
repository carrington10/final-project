from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.
'''
Model class for users to sign up and create profiles 
'''
class UserProfile(models.Model):
       user =models.OneToOneField(User,on_delete=models.CASCADE,)
       name = models.CharField(max_length=30,default='');
       email = models.CharField(max_length=30,default='');
       city = models.CharField(max_length=20,default='');
       bio  = models.TextField(default='');
       favanime = models.CharField(max_length=30,default='');
       image = models.ImageField(upload_to='profile_image',blank=True,default='profile_image/default.jpg')
       def __str__(self):
           return self.user.username
# saves the user profile informations when creating a user profile
def create_profile(sender, **kwargs):
        if kwargs['created']:
                user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender = User)

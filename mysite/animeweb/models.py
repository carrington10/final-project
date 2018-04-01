from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.

# create user and save to datatbase

class UserProfile(models.Model):
       user =models.OneToOneField(User,on_delete=models.CASCADE,)
       description= models.CharField(max_length=100, default='')
       name = models.CharField(max_length=30)
def create_profile(sender, **kwargs):
        if kwargs['created']:
                user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender = User)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments',on_delete = models.CASCADE)
    creator = models.CharField(max_length=200,default="")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,related_name='owner',null = True,on_delete = models.CASCADE)

    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,created = cls.objects.get_or_create(
         current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod

    def lose_friend(cls,current_user,new_friend):
        friend,created = cls.objects.get_or_create(
        current_user = current_user
        )
        friend.users.remove(new_friend)

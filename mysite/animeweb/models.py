from django.db import models
from django.contrib.auth.models import User
# Create your models here.


'''
Model for making and Posting video
'''
class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=50,default="")
    description = models.TextField(max_length=300,default="")
    video=models.FileField(upload_to='videos',null=True,verbose_name="")
    image = models.ImageField(upload_to='popimage',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title + ": " + str(self.video)
'''
Model for making comments
'''
class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments',on_delete = models.CASCADE)
    creator = models.CharField(max_length=200,default="")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

'''
Model for making wall posts to the users profile
'''
class Wallpost(models.Model):

                    user = models.ForeignKey(User,on_delete = models.CASCADE)
                    to_user =  models.ForeignKey(User,related_name='to_user',on_delete = models.CASCADE)
                    wall =  models.TextField(max_length=100,default="")
                    day_created = models.DateTimeField(auto_now_add=True)



                    def __str__(self):
                            return self.wall

'''
Model for adding, and removing friends 
'''
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

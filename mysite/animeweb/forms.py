from django import forms
from animeweb.models import Post, Comment, Wallpost
<<<<<<< HEAD
=======

>>>>>>> 3d33c111dd033beb7c5a0a2a52f6c96134471b53



'''
Form for adding and registering user video posts
'''
class HomeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','description','video','image',)
'''
Form for adding and registering user comments
'''
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
<<<<<<< HEAD
'''
Form for adding and registering wall posts to the current users profile 
'''
=======

>>>>>>> 3d33c111dd033beb7c5a0a2a52f6c96134471b53
class WallForm(forms.ModelForm):

    class Meta:
            model = Wallpost
            fields =('wall',)

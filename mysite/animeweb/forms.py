from django import forms
from animeweb.models import Post, Comment, Wallpost



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
'''
Form for adding and registering wall posts to the current users profile 
'''
class WallForm(forms.ModelForm):

    class Meta:
            model = Wallpost
            fields =('wall',)

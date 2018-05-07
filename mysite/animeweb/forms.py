from django import forms
from animeweb.models import Post, Comment, Wallpost




class HomeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','description','video','image',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class WallForm(forms.ModelForm):

    class Meta:
            model = Wallpost
            fields =('wall',)

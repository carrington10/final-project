from django import forms
from animeweb.models import Post, Comment



class HomeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','description','video')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

from django import forms
from django.forms import ModelForm
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']


class CommentForm(forms.ModelForm):
    

    class Meta:
        model = Comments
        fields = ('name',)
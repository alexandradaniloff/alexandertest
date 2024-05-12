from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Post, Comment


class PostForm(forms.ModelForm):
    #description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [ 'title', 'content', 'type', 'price', 'image']



class CommentForm(forms.ModelForm):
    #description = forms.CharField(min_length=20)

    class Meta:
        model = Comment
        fields = ['post', 'content']
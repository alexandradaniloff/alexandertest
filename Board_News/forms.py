from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Comment, Author


class PostForm(forms.ModelForm):
    #description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'type', 'price', 'image']

class CommentForm(forms.ModelForm):
    #description = forms.CharField(min_length=20)

    class Meta:
        model = Comment
        fields = ['post', 'author', 'content']
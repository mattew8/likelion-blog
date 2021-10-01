from django import forms
from django.db.models import fields
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category','title','content',]
        widgets = {
            'content' : SummernoteWidget()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','password','content']

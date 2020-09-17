from django import forms
from .models import Comment, Post, Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'John Doe'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type in your comment', 'rows':5})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'content', 'images')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of your Post'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'})
        }

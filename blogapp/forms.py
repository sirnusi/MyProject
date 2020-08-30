from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control', 
    'placeholder':'Type your name'}))
    content = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'class':'form-control', 
    'placeholder':'Comment on this post', 'rows':6}))
    class Meta:
        model = Comment
        fields = ('name', 'content',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'content', 'images')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of your Post'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'})
        }
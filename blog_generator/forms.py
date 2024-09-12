# blog_generator/forms.py

from django import forms
from .models import Author, Blog


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'keywords', 'theme', 'tone']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'keywords': forms.Textarea(attrs={'rows': 3}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'theme', 'keywords']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Markdown text'}),
            'keywords': forms.TextInput(attrs={'placeholder': 'Comma-separated keywords'}),
        }

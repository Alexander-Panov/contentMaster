# blog_generator/forms.py

from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'keywords', 'theme', 'tone']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'keywords': forms.Textarea(attrs={'rows': 3}),
        }

# blog_generator/forms.py

from django import forms
from .models import AuthorProfile


class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = ['name', 'bio', 'vocabulary', 'theme', 'tone']

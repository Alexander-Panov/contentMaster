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


class ContentGenerationForm(forms.Form):
    theme = forms.CharField(
        label='Тематика',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    keywords = forms.CharField(
        label='Ключевые слова',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    length = forms.IntegerField(
        label='Объем текста (в словах)',
        min_value=100,
        max_value=2000,
        initial=500,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def clean_keywords(self):
        keywords = self.cleaned_data['keywords']
        # Разделяем ключевые слова запятыми и удаляем лишние пробелы
        return ', '.join([keyword.strip() for keyword in keywords.split(',')])

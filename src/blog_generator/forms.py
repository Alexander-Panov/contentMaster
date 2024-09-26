# blog_generator/forms.py

from django import forms

from .blog.blog_configs import MODELS, LANGUAGES, STYLES
from .models import Author, Blog


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'phrases', 'niche', 'tone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phrases': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'niche': forms.TextInput(attrs={'class': 'form-control'}),
            'tone': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Имя автора',
            'bio': 'Биография',
            'phrases': 'Ключевые слова',
            'niche': 'Тематика',
            'tone': 'Тональность',
        }
        help_texts = {
            'phrases': 'Введите ключевые слова, разделенные запятыми',
            'tone': 'Выберите общую тональность текстов автора',
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['topic', 'niche', 'content', 'language', 'author']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 30}),
            'niche': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'topic': 'Тема',
            'niche': 'Тематика',
            'content': 'Содержание',
            'language': 'Язык',
            'author': 'Автор',
        }
        help_texts = {
        }


class ContentGenerationForm(forms.Form):
    author_id = forms.IntegerField(widget=forms.HiddenInput())
    niche = forms.CharField(
        label='Тематика',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    keywords = forms.CharField(
        label='Ключевые слова',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    word_count = forms.IntegerField(
        label='Объем текста (в словах)',
        min_value=100,
        max_value=2000,
        initial=500,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    topic = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    language_model = forms.ChoiceField(
        label='Языковая модель',
        choices=[(model, model) for model in MODELS],
        initial='openai/gpt-4o-mini',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    language = forms.ChoiceField(
        label='Язык',
        choices=LANGUAGES,
        initial='russian',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    style = forms.ChoiceField(
        label='Стиль',
        choices=STYLES,
        initial='none',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def clean_keywords(self):
        keywords = self.cleaned_data['keywords']
        # Разделяем ключевые слова запятыми и удаляем лишние пробелы
        return ', '.join([keyword.strip() for keyword in keywords.split(',')])

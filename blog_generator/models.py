from django.db import models

# Create your models here.
# blog_generator/models.py

from django.db import models


class AuthorProfile(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    keywords = models.TextField()  # Словарный запас
    theme = models.CharField(max_length=255)
    tone = models.CharField(max_length=50, choices=[('formal', 'Formal'), ('informal', 'Informal')])


class Article(models.Model):
    author_profile = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

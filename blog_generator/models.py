from django.db import models

# Create your models here.
# blog_generator/models.py

from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    keywords = models.TextField()  # Словарный запас
    theme = models.CharField(max_length=255)
    tone = models.CharField(max_length=50, choices=[('formal', 'Formal'), ('informal', 'Informal')])

    def __str__(self):
        return self.name


class CelebrityAuthor(models.Model):
    author = models.OneToOneField(Author(), related_name="celebrity_author", on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name


class ProfileAuthor(models.Model):
    author = models.OneToOneField(Author(), related_name="profile_author", on_delete=models.CASCADE)

    def __str__(self):
        return self.author.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()
    theme = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

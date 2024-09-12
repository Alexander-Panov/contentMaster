from django.shortcuts import render

# Create your views here.
# blog_generator/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, CelebrityAuthor, ProfileAuthor, Blog
from .forms import AuthorForm, BlogForm


def home(request):
    return render(request, 'home.html')


def authors(request):
    user_profiles = ProfileAuthor.objects.all().select_related('author')
    celebrities = CelebrityAuthor.objects.all().select_related('author')
    return render(request, 'authors/list.html', {'user_profiles': user_profiles, 'celebrities': celebrities})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'authors/detail.html', {'author': author})


def create_or_edit_profile(request, profile_id=None):
    if profile_id:
        profile = get_object_or_404(ProfileAuthor, author_id=profile_id).author
    else:
        profile = Author()

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm(instance=profile)

    return render(request, 'authors/form.html', {'form': form})


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blogs/list.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blogs/detail.html', {'blog': blog})


def create_or_edit_blog(request, slug=None):
    if slug:
        blog = get_object_or_404(Blog, slug=slug)
    else:
        blog = None

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blogs/form.html', {'form': form, 'blog': blog})

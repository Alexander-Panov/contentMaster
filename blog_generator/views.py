from django.shortcuts import render

# Create your views here.
# blog_generator/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, CelebrityAuthor, ProfileAuthor
from .forms import AuthorForm


def home(request):
    user_profiles = ProfileAuthor.objects.all().select_related('author')
    celebrities = CelebrityAuthor.objects.all().select_related('author')
    return render(request, 'authors/home.html', {'user_profiles': user_profiles, 'celebrities': celebrities})


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

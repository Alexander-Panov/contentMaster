from django.http import JsonResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async

# Create your views here.
# blog_generator/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .ai.generate_blog import generate_blog
from .ai.generate_blog_mock import generate_blog_mock
from .models import Author, CelebrityAuthor, ProfileAuthor, Blog
from .forms import AuthorForm, BlogForm, ContentGenerationForm


def home(request):
    form = ContentGenerationForm()
    return render(request, 'home.html', {'form': form})


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
            return redirect('author_detail', profile_id)
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
        # Проверяем, есть ли сгенерированные данные в сессии
        generated_data = request.session.pop('generated_blog_data', None)
        if generated_data and not blog:
            form = BlogForm(initial=generated_data)
        else:
            form = BlogForm(instance=blog)

    return render(request, 'blogs/form.html', {'form': form, 'blog': blog})


async def generate_content(request):
    if request.method == 'POST':
        form = ContentGenerationForm(request.POST)
        if form.is_valid():
            theme = form.cleaned_data['theme']
            keywords = form.cleaned_data['keywords']
            length = form.cleaned_data['length']
            # Вызов асинхронной функции generate_blog
            try:
                # generated_content = await generate_blog(theme, keywords.split(','), length)
                generated_content = await generate_blog_mock("theme", theme, keywords.split(','), length)

                # Создание нового блога с сгенерированным контентом

                blog_data = {
                    'title': f"Сгенерированная статья: {theme}",
                    'content': generated_content,
                    'theme': theme,
                    'keywords': keywords,
                }

                def save_data_to_session():
                    # Сохраняем данные в сессии
                    request.session['generated_blog_data'] = blog_data

                await sync_to_async(save_data_to_session)()

                return JsonResponse({'success': True, 'redirect_url': reverse('create_blog')})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
    else:
        form = ContentGenerationForm()

    return render(request, 'blogs/generate_blog.html', {'form': form})


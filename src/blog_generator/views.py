from django.http import JsonResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from django.conf import settings

from .blog.blog_configs import MODELS, LANGUAGES, STYLES
from .blog.generate_blog import generate_blog_topics, generate_blog
from .blog.generate_blog_mock import generate_blog_mock, generate_blog_topics_mock
from .blog.utils import clear_markdown, word_statistics, symbol_statistics, keywords_statistics
from .models import Author, CelebrityAuthor, ProfileAuthor, Blog
from .forms import AuthorForm, BlogForm, ContentGenerationForm


def home(request):
    form = ContentGenerationForm()
    return render(request, 'home.html', {'form': form})


def author_list(request):
    user_profiles = ProfileAuthor.objects.all().select_related('author').order_by('-author_id')
    celebrities = CelebrityAuthor.objects.all().select_related('author').order_by('-author_id')
    return render(request, 'authors/list.html', {'user_profiles': user_profiles, 'celebrities': celebrities})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'authors/detail.html', {'author': author})


def select_author(request, author_id):
    author = Author.objects.get(id=author_id)
    form = ContentGenerationForm(initial={'author_id': author.id})
    return render(request, 'blogs/generate_blog.html', {'form': form})


def create_or_edit_profile(request, profile_id=None):
    if profile_id:
        profile = get_object_or_404(ProfileAuthor, author_id=profile_id).author
    else:
        profile = Author()

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            ProfileAuthor.objects.create(author=profile)
            return redirect('author_detail', profile.id)
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


@require_POST
async def generate_topics(request):
    form = ContentGenerationForm(request.POST)
    form.is_valid()
    if any(key in form.cleaned_data.keys() for key in
           ['niche', 'keywords', 'word_count', 'language_model', 'language', 'style']):
        niche = form.cleaned_data['niche']
        keywords = form.cleaned_data['keywords']
        word_count = form.cleaned_data['word_count']

        language_model = form.cleaned_data['language_model']
        language = form.cleaned_data['language']
        style = form.cleaned_data['style']
        try:
            if settings.TEST:
                generate_blog_topics_function = generate_blog_topics_mock
            else:
                generate_blog_topics_function = generate_blog_topics
            # noinspection PyUnboundLocalVariable
            topics = await generate_blog_topics_function(niche, keywords.split(','), word_count, language_model,
                                                         language,
                                                         style)

            return JsonResponse({'success': True, 'topics': topics})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return render(request, 'blogs/generate_blog.html', {'form': form})


@require_POST
async def generate_content(request):
    form = ContentGenerationForm(request.POST)
    if form.is_valid():
        topic = form.cleaned_data['topic']
        niche = form.cleaned_data['niche']
        keywords = form.cleaned_data['keywords']
        word_count = form.cleaned_data['word_count']
        author_id = form.cleaned_data['author_id']
        language_model = form.cleaned_data['language_model']
        language = form.cleaned_data['language']
        style = form.cleaned_data['style']

        # Вызов асинхронной функции generate_blog
        try:
            author = await sync_to_async(Author.objects.get)(id=author_id)

            if settings.TEST:
                generate_blog_function = generate_blog_mock
            else:
                generate_blog_function = generate_blog

            generated_content = await generate_blog_function(niche, topic, keywords.split(','), word_count, author,
                                                             language_model,
                                                             language,
                                                             style)

            # Создание нового блога со сгенерированным контентом
            new_blog = await sync_to_async(Blog.objects.create)(
                topic=topic,
                author=author,
                content=generated_content,
                niche=niche,
                language=language
            )

            return JsonResponse({'success': True, 'redirect_url': reverse('blog_detail', args=[new_blog.slug])})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'blogs/generate_blog.html', {'form': form,
                                                        'models': MODELS,
                                                        'languages': LANGUAGES,
                                                        'styles': STYLES})


def blog_analytics(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    cleared_content = clear_markdown(blog.content)

    analytics = {
        'word_count': word_statistics(cleared_content),
        'symbol_count': symbol_statistics(cleared_content),
        'keywords': keywords_statistics(cleared_content, lang=blog.language)
    }

    return JsonResponse(analytics)
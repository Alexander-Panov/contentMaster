from django.urls import path

from blog_generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/', views.authors, name='author_list'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('author/new/', views.create_or_edit_profile, name='create_author'),
    path('author/edit/<int:profile_id>/', views.create_or_edit_profile, name='edit_author'),

    path('blog/', views.blog_list, name='blog_list'),
    path('blog/new/', views.create_or_edit_blog, name='create_blog'),
    path('blog/edit/<slug:slug>/', views.create_or_edit_blog, name='edit_blog'),
    path('blog/generate/', views.generate_content, name='generate_blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]

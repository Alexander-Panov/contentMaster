from django.urls import path

from blog_generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('author/new/', views.create_or_edit_profile, name='create_or_edit_profile'),
    path('author/edit/<int:profile_id>/', views.create_or_edit_profile, name='create_or_edit_profile'),
]

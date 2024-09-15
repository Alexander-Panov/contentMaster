from django.contrib import admin

from blog_generator.models import Author, CelebrityAuthor, ProfileAuthor, Blog


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(CelebrityAuthor)
class CelebrityAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileAuthor)
class ProfileAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

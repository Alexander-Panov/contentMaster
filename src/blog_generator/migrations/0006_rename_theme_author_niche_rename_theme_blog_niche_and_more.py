# Generated by Django 5.1.1 on 2024-09-13 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_generator', '0005_blog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='theme',
            new_name='niche',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='theme',
            new_name='niche',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='topic',
        ),
    ]

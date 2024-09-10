# Generated by Django 5.1.1 on 2024-09-10 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('keywords', models.TextField()),
                ('theme', models.CharField(max_length=255)),
                ('tone', models.CharField(choices=[('formal', 'Formal'), ('informal', 'Informal')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_generator.author')),
            ],
        ),
        migrations.CreateModel(
            name='CelebrityAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog_generator.author')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_generator', '0007_rename_keywords_author_phrases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='keywords',
        ),
        migrations.AddField(
            model_name='blog',
            name='language',
            field=models.CharField(choices=[('russian', 'Русский'), ('english', 'Английский'), ('spanish', 'Испанский'), ('chinese', 'Китайский')], default='russian', max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='tone',
            field=models.CharField(choices=[('formal', 'Формальный'), ('informal', 'Не формальный')], max_length=50),
        ),
    ]

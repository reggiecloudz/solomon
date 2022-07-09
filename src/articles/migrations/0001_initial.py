# Generated by Django 3.2.13 on 2022-07-09 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('video_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='video url')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('slug', models.SlugField(unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='articles.article')),
                ('user', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article')),
                ('author', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='articles.comment')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]

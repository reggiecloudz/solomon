# Generated by Django 3.2.13 on 2022-07-21 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(blank=True, max_length=255, verbose_name='response')),
                ('explanation', models.TextField(blank=True, verbose_name='explanation')),
                ('is_read', models.BooleanField(blank=True, default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=144, verbose_name='label')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_complete', models.BooleanField(blank=True, default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to='accounts.client')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='questions.answer')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'reply',
                'verbose_name_plural': 'replies',
            },
        ),
        migrations.CreateModel(
            name='QuestionnaireItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=144, verbose_name='question')),
                ('is_answered', models.BooleanField(blank=True, default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('questionnaire', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='questions.questionnaire')),
            ],
            options={
                'verbose_name': 'questionnaire item',
                'verbose_name_plural': 'questionnaire items',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiry', models.CharField(blank=True, max_length=255, verbose_name='inquiry')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('is_answered', models.BooleanField(blank=True, default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='questions.question'),
        ),
    ]

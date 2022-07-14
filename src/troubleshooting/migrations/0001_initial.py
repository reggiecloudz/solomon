# Generated by Django 3.2.13 on 2022-07-13 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incidents', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=144)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('incident', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='incidents.incident')),
                ('technician', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='accounts.technician')),
            ],
            options={
                'verbose_name': 'solution',
                'verbose_name_plural': 'solutions',
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=144)),
                ('step_number', models.PositiveSmallIntegerField(blank=True)),
                ('is_complete', models.BooleanField(blank=True, default=False)),
                ('documentation', models.JSONField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solution', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='troubleshooting.solution')),
            ],
            options={
                'verbose_name': 'step',
                'verbose_name_plural': 'steps',
            },
        ),
    ]
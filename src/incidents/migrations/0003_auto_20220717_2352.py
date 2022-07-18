# Generated by Django 3.2.13 on 2022-07-17 23:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0002_alter_job_hours_worked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='label',
        ),
        migrations.RemoveField(
            model_name='action',
            name='solution',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='job',
        ),
        migrations.RemoveField(
            model_name='implementation',
            name='job',
        ),
        migrations.AddField(
            model_name='action',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='incidents.action'),
        ),
        migrations.AddField(
            model_name='action',
            name='progress',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='progress'),
        ),
        migrations.AddField(
            model_name='action',
            name='task',
            field=models.CharField(blank=True, max_length=144, verbose_name='task'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='appointment date'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='label',
            field=models.CharField(blank=True, max_length=75, verbose_name='label'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='support_request',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='support_requests', to='incidents.supportrequest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='was_accepted',
            field=models.BooleanField(blank=True, default=False, verbose_name='was accepted'),
        ),
        migrations.AddField(
            model_name='implementation',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='implementation',
            name='plan',
            field=models.TextField(blank=True, verbose_name='plan'),
        ),
        migrations.AddField(
            model_name='implementation',
            name='solution',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='implementation', to='incidents.solution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='implementation',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date'),
        ),
        migrations.AddField(
            model_name='implementation',
            name='tools',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='solution',
            name='is_selected',
            field=models.BooleanField(blank=True, default=False, verbose_name='is selected'),
        ),
        migrations.AddField(
            model_name='solution',
            name='label',
            field=models.CharField(blank=True, max_length=144, verbose_name='label'),
        ),
        migrations.AddField(
            model_name='solution',
            name='overall_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, verbose_name='hourly rate'),
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=144, verbose_name='label')),
                ('is_complete', models.BooleanField(blank=True, default=False, verbose_name='is complete')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('implementation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='phases', to='incidents.implementation')),
            ],
            options={
                'verbose_name': 'phase',
                'verbose_name_plural': 'phases',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='phase',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='incidents.phase'),
            preserve_default=False,
        ),
    ]

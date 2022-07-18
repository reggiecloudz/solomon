# Generated by Django 3.2.13 on 2022-07-17 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('assets', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_passed', models.BooleanField(blank=True, default=False, verbose_name='all passed')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'evaluation',
                'verbose_name_plural': 'evaluations',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=75, verbose_name='label')),
                ('priority', models.CharField(blank=True, choices=[('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low')], max_length=20, verbose_name='priority')),
                ('status', models.CharField(blank=True, choices=[('Created', 'Created'), ('Working', 'Working'), ('Paused', 'Paused'), ('Completed', 'Completed'), ('Resolved', 'Resolved'), ('Unresolved', 'Unresolved')], default='Created', max_length=20, verbose_name='status')),
                ('hours_worked', models.FloatField(blank=True, null=True, verbose_name='hours worked')),
                ('documentation', models.JSONField(blank=True, default=list, null=True)),
                ('work_periods', models.JSONField(blank=True, default=list, null=True, verbose_name='work periods')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='SupportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(blank=True, verbose_name='problem')),
                ('details', models.TextField(blank=True, null=True, verbose_name='details')),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='hourly rate')),
                ('documentation', models.JSONField(blank=True, default=list, null=True)),
                ('followup_dates', models.JSONField(blank=True, default=list, null=True)),
                ('status', models.CharField(blank=True, choices=[('Submitted', 'Submitted'), ('Review', 'Review'), ('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Offer', 'Offer'), ('Agreed', 'Agreed'), ('Disagreed', 'Disagreed'), ('Scheduled', 'Scheduled'), ('Working', 'Working'), ('Paused', 'Paused')], default='Submitted', max_length=50, verbose_name='status')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='support_requests', to='accounts.client')),
                ('device', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='support_requests', to='assets.device')),
                ('questionnaire', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='support_request', to='questions.questionnaire')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='support_requests', to='accounts.technician')),
            ],
            options={
                'verbose_name': 'support request',
                'verbose_name_plural': 'support requests',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='incidents.job')),
            ],
            options={
                'verbose_name': 'solution',
                'verbose_name_plural': 'solutions',
            },
        ),
        migrations.CreateModel(
            name='RootCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(blank=True, max_length=144, verbose_name='cause')),
                ('findings', models.TextField(blank=True, null=True, verbose_name='findings')),
                ('documentation', models.JSONField(blank=True, default=list, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_cause', to='incidents.job')),
            ],
            options={
                'verbose_name': 'root cause',
                'verbose_name_plural': 'root causes',
            },
        ),
        migrations.CreateModel(
            name='ProblemDefinition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(blank=True, verbose_name='context')),
                ('background', models.TextField(blank=True, verbose_name='background')),
                ('symptoms', models.TextField(blank=True, verbose_name='symptoms')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='problem_definition', to='incidents.job')),
            ],
            options={
                'verbose_name': 'problem definition',
                'verbose_name_plural': 'problem definitions',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='support_request',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='incidents.supportrequest'),
        ),
        migrations.AddField(
            model_name='job',
            name='technician',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='accounts.technician'),
        ),
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='implementation', to='incidents.job')),
            ],
            options={
                'verbose_name': 'implementation',
                'verbose_name_plural': 'implementations',
            },
        ),
        migrations.CreateModel(
            name='EvaluationTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=144, verbose_name='task')),
                ('passed', models.BooleanField(blank=True, default=False)),
                ('results', models.TextField(blank=True, null=True, verbose_name='results')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('evaluation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='incidents.evaluation', verbose_name='evaluation')),
            ],
            options={
                'verbose_name': 'evaluation test',
                'verbose_name_plural': 'evaluation tests',
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='job',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='incidents.job'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='incidents.job')),
            ],
            options={
                'verbose_name': 'appointment',
                'verbose_name_plural': 'appointments',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=144, verbose_name='label')),
                ('is_complete', models.BooleanField(blank=True, default=False)),
                ('is_milestone', models.BooleanField(blank=True, default=False)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('solution', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='incidents.solution')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions', to='accounts.technician')),
            ],
            options={
                'verbose_name': 'action',
                'verbose_name_plural': 'actions',
            },
        ),
    ]

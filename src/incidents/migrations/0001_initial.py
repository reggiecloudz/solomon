# Generated by Django 3.2.13 on 2022-07-13 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=144)),
                ('explanation', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('Submitted', 'Submitted'), ('Review', 'Review'), ('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Agreed', 'Agreed'), ('Disagreed', 'Disagreed'), ('Waiting', 'Waiting'), ('Working', 'Working'), ('Completed', 'Completed'), ('Evaluation', 'Evaluation'), ('Resolved', 'Resolved'), ('Unresolved', 'Unresolved')], default='Submitted', max_length=60)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('resolved_date', models.DateField(blank=True, null=True)),
                ('start_work_time', models.TimeField(blank=True, null=True)),
                ('end_work_time', models.TimeField(blank=True, null=True)),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to='accounts.client')),
                ('device', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to='assets.device')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incidents', to='accounts.technician')),
            ],
            options={
                'verbose_name': 'incident',
                'verbose_name_plural': 'incidents',
            },
        ),
    ]

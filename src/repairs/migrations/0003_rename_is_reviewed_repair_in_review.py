# Generated by Django 3.2.13 on 2022-07-10 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_repair_is_reviewed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repair',
            old_name='is_reviewed',
            new_name='in_review',
        ),
    ]

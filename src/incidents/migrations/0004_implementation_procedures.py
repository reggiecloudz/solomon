# Generated by Django 3.2.13 on 2022-07-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0003_auto_20220723_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='implementation',
            name='procedures',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
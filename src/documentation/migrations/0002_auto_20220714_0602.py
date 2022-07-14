# Generated by Django 3.2.13 on 2022-07-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemdescription',
            options={'verbose_name': 'system description', 'verbose_name_plural': 'system descriptions'},
        ),
        migrations.AlterField(
            model_name='systemdescription',
            name='hard_drives',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='systemdescription',
            name='operating_system',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='systemdescription',
            name='pci_slots',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
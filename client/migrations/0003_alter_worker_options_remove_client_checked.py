# Generated by Django 5.0.6 on 2024-05-13 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_worker_client_status_client_worker'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'Ishchi | Worker', 'verbose_name_plural': 'Ishchilar | Workers'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='checked',
        ),
    ]

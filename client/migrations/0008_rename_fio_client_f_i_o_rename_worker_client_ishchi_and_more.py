# Generated by Django 5.0.6 on 2024-05-15 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_client_options_alter_worker_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='FIO',
            new_name='F_I_O',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='worker',
            new_name='ishchi',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phone_number',
            new_name='telefon_raqam',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-15 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_rename_fio_client_f_i_o_rename_worker_client_ishchi_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='F_I_O',
            new_name='f_i_o',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='created_at',
            new_name='zayafka_vaqti',
        ),
    ]

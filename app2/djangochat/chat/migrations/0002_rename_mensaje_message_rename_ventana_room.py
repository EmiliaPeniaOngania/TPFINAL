# Generated by Django 4.1 on 2022-10-11 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mensaje',
            new_name='Message',
        ),
        migrations.RenameModel(
            old_name='Ventana',
            new_name='Room',
        ),
    ]
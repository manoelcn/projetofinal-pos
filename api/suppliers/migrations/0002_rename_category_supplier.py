# Generated by Django 5.1.4 on 2024-12-13 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Supplier',
        ),
    ]

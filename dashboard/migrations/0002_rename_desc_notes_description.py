# Generated by Django 5.0.1 on 2024-01-19 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='desc',
            new_name='description',
        ),
    ]

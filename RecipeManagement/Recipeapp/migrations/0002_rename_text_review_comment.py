# Generated by Django 5.0.3 on 2024-03-11 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='comment',
        ),
    ]

# Generated by Django 3.2.9 on 2023-01-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='project_slug', max_length=520),
        ),
    ]

# Generated by Django 3.2.9 on 2022-12-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects/static/images/'),
        ),
    ]

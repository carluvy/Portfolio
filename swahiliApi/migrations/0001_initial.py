# Generated by Django 3.2.9 on 2022-12-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('translation', models.CharField(max_length=80)),
            ],
        ),
    ]

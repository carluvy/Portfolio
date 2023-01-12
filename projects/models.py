from django.conf import settings
from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
    github_url = models.URLField(default='github_url', max_length=250)
    medium_url = models.URLField(default='medium_url')

    def __str__(self) -> str:
        return f"{self.title}: {self.description}"

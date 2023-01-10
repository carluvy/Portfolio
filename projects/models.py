from django.conf import settings
from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)

    def __str__(self) -> str:
        return f"{self.title}: {self.description}"

from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
    github_url = models.URLField(default='githuburl', max_length=200)
    medium_url = models.URLField(default='mediumurl', max_length=200)

    # slug = models.SlugField(max_length=520, )

    def __str__(self) -> str:
        return self.title
        # return reverse('index', args=[str(self.title)])
        # return f"{self.title}: {self.description}"

    # def get_absolute_url(self):
    #     #     # return reverse('index',
    #     #     #                kwargs={'slug': self.slug})
    #     return f'index/{self.title}'

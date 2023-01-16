from django.conf import settings
from django.db import models


# Create your models here.
class About(models.Model):
    profile_pic = models.FilePathField(path=settings.PROFILE_PIC_PATH)

    def __str__(self) -> str:
        return f"{self.profile_pic}"



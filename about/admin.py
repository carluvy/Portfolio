from django.contrib import admin

# Register your models here.
from about.models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    field = ("profile_pic",)

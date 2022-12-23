from django.contrib import admin


# Register your models here.
from swahiliApi.models import Word


@admin.register(Word)
class SwahiliApiAdmin(admin.ModelAdmin):
    list_display = ("word", "state", "translation")

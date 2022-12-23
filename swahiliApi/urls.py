from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.WordListAPIView.as_view(), name="words_list"),
    path("create/", CreateWordAPIView.as_view(), name="word_create"),
    path("update/<int:pk>/", UpdateWordAPIView.as_view(), name="update_word"),
    path("delete/<int:pk>/", DeleteWordAPIView.as_view(), name="delete_word"),
]

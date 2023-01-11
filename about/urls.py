from django.urls import path

from about import views


urlpatterns = [
    path("", views.about_me, name='about-me'),
]

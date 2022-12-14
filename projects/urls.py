from django.conf.urls.static import static
from django.contrib.auth import admin
from django.urls import path

from personal_portfolio import settings
from . import views
from .views import SearchResultsView

urlpatterns = [
    path("", views.project_index, name="index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    # path("search/", views.project_search, name="search_projects"),
    path("search/", SearchResultsView.as_view(), name='search_projects'),

]


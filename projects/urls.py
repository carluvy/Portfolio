from django.urls import path

from . import views
from .views import SearchResultsView, ProjectView, ProjectDetail

urlpatterns = [
    path("", ProjectView.as_view(), name="project_list"),
    path("<int:pk>/", ProjectDetail.as_view(), name="project_detail"),
    # path("search/", views.project_search, name="search_projects"),
    path("search/", SearchResultsView.as_view(), name='search_projects', )
]

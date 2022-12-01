from django.urls import path

from . import views
from .views import BlogView

urlpatterns = [
    path("", BlogView.as_view(), name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
    # path("search/", views.search_blogs, name="search_blogs"),
    # path("search/", SearchResultsView.as_view(), name="search_results"),

]

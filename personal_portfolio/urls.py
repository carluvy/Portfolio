"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from rest_framework.documentation import include_docs_urls

from personal_portfolio.sitemaps import ProjectSitemap, BlogSitemap

sitemaps = {
    'portfolio': ProjectSitemap,
    'blog': BlogSitemap,
}
urlpatterns = [

                  path("admin/", admin.site.urls),

                  path('docs/', include_docs_urls(title='Swahili API')),
                  path("words/", include("swahiliApi.urls")),
                  path("", include("about.urls")),

                  path("portfolio/", include("projects.urls")),
                  path("blog/", include("blog.urls")),
                  path("user/", include("users.urls")),
                  path("password_reset/done/",
                       auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(
                           template_name="registration/password_reset_confirm.html"),
                       name='password_reset_confirm'),
                  path('reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(
                           template_name='registration/password_reset_complete.html'),
                       name='password_reset_complete'),
                  path("accounts/", include("allauth.urls")),
                  re_path(r'^robots\.txt', include('robots.urls')),
                  path('sitemap.xml', sitemap,
                       {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

                  # new
                  # {'sitemaps': {'projects': GenericSitemap(projects, priority=0.8)}},
                  # name='django.contrib.sitemaps.views.sitemap'),

                  # path('social-auth/', include('allauth.socialaccount.providers.google.urls'))
                  # path("search/", views.search_blogs(search_params='data', request=raw_input), name="search_results"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

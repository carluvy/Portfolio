from django.contrib.sitemaps import Sitemap


from blog.models import Post
from projects.models import Project


class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Project.objects.all()

    # def lastmod(self, obj):
    #     return obj.project_published

    def location(self, obj):
        return '/portfolio/%s' % obj.title


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.last_modified

    def location(self, obj):
        return '/blog/%s' % obj.title

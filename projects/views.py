from django.contrib import messages
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline, SearchRank
from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from blog.models import Post
from projects.forms import PostSearchForm
from projects.models import Project


# class ProjectBaseView(View):
#     model = Project
#     # for m in model.objects.all():
#     # print("file paths for the images is:", m.image)
#     success_url = reverse_lazy('index')
#
#
# class ProjectView(ProjectBaseView, ListView):
#     template_name = 'index.html'


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'index.html', context)


# class ProjectDetail(DetailView):
#     model = Project
#     template_name = 'project_detail.html'


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


# def search_projects(request):
#     if request.method == 'POST':
#         vector = SearchVector('body')
#         queried = request.POST['queried']
#
#         blog_entries = Post.objects.annotate(
#             v_head=SearchHeadline(F('body'), queried)
#         ).filter(title=vector)
#
#         blogs = Post.objects.filter(body__search=queried)
#
#         context = {
#             'queried': queried,
#             'blogs': blog_entries, }
#         return render(request, "search_project.html", context)
#     else:
#         return render(request, "search_project.html", {})


# def project_search(request):
#     form = PostSearchForm()
#     blogs = []
#     if 'queried' in request.GET:
#         form = PostSearchForm(request.GET)
#         if form.is_valid():
#             queried = form.cleaned_data['queried']
#             # print(queried)
#             # blogs = Post.objects.filter(body__icontains=queried)
#             query = SearchQuery(queried)
#             vector = SearchVector('body')
#
#             # blogs = Post.objects.annotate(search=SearchVector('title', 'body'),
#             #                               ).filter(search=queried)
#             blogs = Post.objects.annotate(
#                 search=vector,
#                 headline=SearchHeadline('body', query)).filter(search=query)
#     return render(request, "search_project.html", {'form': form, 'blogs': blogs, 'queried': queried})


class SearchResultsView(ListView):
    form_class = PostSearchForm
    model = Post
    context_object_name = 'blogs'
    template_name = 'search_project.html'

    # blogs = []

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            queried = form.cleaned_data["queried"]
            query = SearchQuery(queried)
            vector = SearchVector('body')
            blogs = Post.objects.annotate(
                search=vector,
                headline=SearchHeadline('body', query)).filter(search=query)
            return blogs

        #         Post.objects.filter(
        #     Q(title__icontains=queried) | Q(body__icontains=queried)
        # )
        # print(object_list)

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(request.GET)
    #     blogs = []
    #     if form.is_valid():
    #         queried = form.cleaned_data['queried']
    #         query = SearchQuery(queried)
    #         vector = SearchVector('body')
    #         blogs = self.model.objects.annotate(
    #             search=vector,
    #             headline=SearchHeadline('body', query)).filter(search=query)
    #         # print(blogs.query)
    #
    #         # return HttpResponseRedirect('/success')
    #     return render(request, self.template_name, {'form': form, 'blogs': blogs})




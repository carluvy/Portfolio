from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import CommentForm
from .models import Post, Comment


class BlogBaseView(View):
    model = Post
    success_url = reverse_lazy('blog_index')


class BlogView(BlogBaseView, ListView):
    template_name = 'blog_index.html'


# def blog_index(request):
#     posts = Post.objects.all().order_by('-created_on')
#     context = {
#         "posts": posts,
#     }
#     return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)




#
# class BlogDetailView(DetailView):
#     comment_form_class = CommentForm
#     model = Post
#     template_name = 'blog_detail.html'
#
#     def post(self, request, *args, **kwargs):
#         form = self.comment_form_class(request.POST)
#         post = Post.objects.get(pk=args)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#                 post=post, )
#
#             comment.save()
#         comments = Comment.objects.filter(post=post)
#         context = {
#             'post': post,
#             'comments': comments,
#             'form': form,
#         }
#
#         return render(request, self.template_name, context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)

# class BlogDetailView(ListView):
#     model = Post
#     template_name = 'blog_category.html'
#
#     def get_queryset(self):
#         return Post.objects.filter()

# def search_blogs(request):
#     if request.method == 'POST':
#         blogs = request.POST['blogs']
#         return render(request=request, template_name="search_blogs.html", context={'blogs': blogs})
#     else:
#         return render(request=request, template_name="search_blogs.html", context='hout')

# post = Post.objects.filter(
#     posts__body__contains=search_params
# ).order_by(
#     '-created_on')
#
# context = {
#     'post': post,
#
#
# class SearchResultsView(ListView):
#     model = Post.objects.filter()
#     template_name = 'search_blogs.html'

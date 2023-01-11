from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from about.models import About


# class AboutMeView(ListView):
#     model = About
#
#     template_name = 'about-me.html'


def about_me(request):
    abouts = About.objects.all()
    context = {
        'abouts': abouts
    }
    # for m in abouts:
    #     print("file paths for the images is:", m.image)

    return render(request, 'about-me.html', context)

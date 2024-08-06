from django.shortcuts import render

from eco.models import HomeModel, ImagesModel, AboutModel


def home_view(request):
    details = HomeModel.objects.all()
    images = ImagesModel.objects.all()
    context = {
        'details': details,
        'images': images
    }
    return render(request, 'index.html', context=context)

def about_page(request):
    about = AboutModel.objects.all()
    context = {
        'abouts': about
    }
    return render(request, 'about.html', context=context)

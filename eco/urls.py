from django.urls import path

from eco.views import home_view, about_page

urlpatterns = [
    path('', home_view),
    path('about/', about_page, name='about'),
]
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import PhotoUploadModelForm

from .models import Post


def converter(reques):
    pass


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):
    form_class = PhotoUploadModelForm
    model = Post
    template_name = 'add.html'

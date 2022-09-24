from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'zblog/index.html')


def index(request):
    posts = Post.objects.all()

    return render(request, 'zblog/index.html',
    {
        'posts':posts,
    })


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'head_img']

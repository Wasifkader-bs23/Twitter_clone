from msilib.schema import ListView
from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
# from matplotlib.style import context
# Create your views here.

posts=[
    {   
        'author': 'John',
        'title': 'BP 1',
        'content': 'First posts',
        'date_posted': 'June 29 2022'
    },
     {   
        'author': 'Wasif',
        'title': 'BP 2',
        'content': 'Second post',
        'date_posted': 'June 29 2022'
    }
    
]

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name= 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
   


def about(request):
    return render(request,'blog/about.html')
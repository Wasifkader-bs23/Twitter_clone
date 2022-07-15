from msilib.schema import ListView
from typing import List
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post= self.get_object()

        if self.request.user == post.author:
            return True
        return False
   
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post= self.get_object()

        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html')
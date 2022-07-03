from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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


def about(request):
    return render(request,'blog/about.html')
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Destiny Franks',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': '7th August 2021',
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is my second blog post',
        'date_posted': '14th August 2021',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})

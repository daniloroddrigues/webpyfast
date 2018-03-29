from django.shortcuts import render
from webpyfast.blogs.models import Blog


def blog(request):
    blogs = Blog()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)

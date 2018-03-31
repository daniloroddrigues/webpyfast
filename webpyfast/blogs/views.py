from django.shortcuts import render
from webpyfast.blogs.models import Blog


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)

from django.shortcuts import render
from webpyfast.blogs.models import Post


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

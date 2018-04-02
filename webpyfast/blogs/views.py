from django.shortcuts import render
from webpyfast.blogs.models import Post


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post.html', context)

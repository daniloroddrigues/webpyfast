from django.shortcuts import render
from webpyfast.blogs.models import Post


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post.html', context)


def post_detail(request, pk, slug):
    post = Post.objects.get(pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post_detail': post})

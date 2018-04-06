from django.shortcuts import render

from webpyfast.blogs.models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)

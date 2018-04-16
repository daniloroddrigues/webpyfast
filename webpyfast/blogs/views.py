from django.shortcuts import render
from webpyfast.blogs.models import Post, Category, Tags


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/post.html', {'posts': posts})


def post_detail(request, pk, slug):
    post = Post.objects.get(pk=pk, slug=slug)
    categories = post.categories.all()
    tags = post.tags.all()
    return render(request, 'blog/post_detail.html', {'post_detail': post, 'categories': categories, 'tags': tags})


def category(request, slug):
    # category = Category.objects.get(slug=slug)
    return render(request, 'blog/category.html', {'categories': Category()})

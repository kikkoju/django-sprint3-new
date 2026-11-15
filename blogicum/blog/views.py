from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category

POST_ON_MAIN_PAGE = 5


def published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    template = 'blog/index.html',
    post_list = published_posts()[:POST_ON_MAIN_PAGE]
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        published_posts(),
        id=id
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )

    post_list = published_posts().filter(
        category=category
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)

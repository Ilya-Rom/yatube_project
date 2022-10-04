from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    """Метод, передающий в шаблон posts/index.html
    десять последних объектов модели Post.
    """
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Метод, передающий в шаблон posts/group_list.html
    десять последних объектов модели Post, отфильтрованных по полю group,
    в случае, если адрес не найден, возвращается код ошибки 404.
    """
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

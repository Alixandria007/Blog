from django.shortcuts import render
from django.core.paginator import Paginator
from blog import models
from django.db.models import Q

# Create your views here.

def index(request):
    posts = (models.Post.objects.filter(is_public = True).order_by('-pk'))

    paginator = Paginator(posts,10)
    page_number = request.GET.get("page",None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }


    return render(request, 'blog/pages/index.html', context)

def post(request, slug):
    post = models.Post.objects.filter(slug = slug).first()


    context = {'post': post}

    return render(request, 'blog/pages/post.html', context)

def page(request):
    return render(request, 'blog/pages/page.html')


def created_by(request, id):
    p = models.Post.objects.all()
    posts = models.Post.objects.filter(created_by__pk = id)
    print(id)
    print(posts)
    print(p)

    paginator = Paginator(posts,10)
    page_number = request.GET.get("page",None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }


    return render(request, 'blog/pages/index.html', context)


def category(request, slug):
    posts = models.Post.objects.filter(category__slug = slug)

    paginator = Paginator(posts,10)
    page_number = request.GET.get("page",None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }


    return render(request, 'blog/pages/index.html', context)


def tag(request, slug):
    posts = models.Post.objects.filter(tag__slug = slug)

    paginator = Paginator(posts,10)
    page_number = request.GET.get("page",None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }


    return render(request, 'blog/pages/index.html', context)

def search(request):
    search = request.GET.get('search','').strip()
    posts = models.Post.objects.filter(Q(title__icontains=search) | Q(excerpt__icontains=search) | Q(content__icontains=search))

    context = {
        'page_obj': posts,
    }


    return render(request, 'blog/pages/index.html', context)
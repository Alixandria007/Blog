from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    posts = 1000

    paginator = Paginator(posts,10)
    page_number = paginator.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }


    return render(request, 'blog/pages/index.html', context)

def post(request):
    return render(request, 'blog/pages/post.html')

def page(request):
    return render(request, 'blog/pages/page.html')
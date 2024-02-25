from django.shortcuts import render
from django.core.paginator import Paginator
from blog import models
from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView
from django.contrib.auth.models import User


# Create your views here.


class IndexListView(ListView):
    template_name = 'blog/pages/index.html'
    context_object_name = 'page_obj'
    paginate_by = 9
    queryset = models.Post.objects.filter(is_public = True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f'Home - '
        return context
    

def post(request, slug):
    posts = models.Post.objects.filter(is_public = True, slug = slug).first()

    if page == None:
        raise Http404()

    context = {'post': posts,
               'page_title':f'{posts.title} - ',}

    return render(request, 'blog/pages/post.html', context)

def page(request,slug):
    page = models.Page.objects.filter(is_public = True, slug = slug).first()

    if page == None:
        raise Http404()

    context = {'page': page,
               'page_title':f'{page.title} - ',
               }
    return render(request, 'blog/pages/page.html',context)


class CreatedByListView(IndexListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._temp_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self._temp_context['user']
        user_full_name = user.username
        print('Argumentos', context)

        page_title = user_full_name + ' - ' + ' Autor - '

        context.update({
            'page_title': page_title,
        })

        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(created_by__pk=self._temp_context['user'].pk)
        return qs
    
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        user = User.objects.filter(pk=id).first()

        if user is None:
            raise Http404()

        self._temp_context.update({
            'id': id,
            'user': user,
        })

        return super().get(request, *args, **kwargs)
    
class CategoryListView(IndexListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._temp_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self._temp_context['category']
        category_name = self.object_list[0].category.name
        print('Argumentos', context)

        page_title = str(category_name) + ' - ' + ' Autor - '

        context.update({
            'page_title': page_title,
        })

        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(category__slug = self._temp_context['slug'])
        return qs
    
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        category = models.Category.objects.filter(slug = slug)

        if slug is None:
            raise Http404()

        self._temp_context.update({
            'slug': slug,
            'category': category,
        })

        return super().get(request, *args, **kwargs)



def category(request, slug):
    posts = models.Post.objects.filter(is_public = True, category__slug = slug)

    paginator = Paginator(posts,10)
    page_number = request.GET.get("page",None)
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    context = {
        'page_obj': page_obj,
        'page_title': f'{posts.first().category.name} - Categoria - '
    }


    return render(request, 'blog/pages/index.html', context)


def tag(request, slug):
    posts = models.Post.objects.filter(is_public = True, tag__slug = slug)

    paginator = Paginator(posts,10)
    page_number = request.GET.get("page",None)
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    context = {
        'page_obj': page_obj,
        'page_title': f'{posts.first().created_by} - Autor - '
    }


    return render(request, 'blog/pages/index.html', context)

def search(request):
    search = request.GET.get('search','').strip()
    posts = models.Post.objects.filter(Q(title__icontains=search) | Q(excerpt__icontains=search) | Q(content__icontains=search))

    context = {
        'page_obj': posts,
        'page_title': f'{search[:30]} - Search - '
    }


    return render(request, 'blog/pages/index.html', context)
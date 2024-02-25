from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from blog import models
from django.db.models import Q
from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView,DetailView
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
    
class PostDatailView(DetailView):
    model = models.Post
    template_name = 'blog/pages/post.html'
    slug_field = 'slug'
    context_object_name = 'post'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset().filter(is_public = True)

        return qs
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.context_object_name == None:
            raise Http404()
        
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = f'{self.object.title} - Post - '
        return context

class PageDatailView(DetailView):
    model = models.Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset().filter(is_public = True)

        return qs
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.context_object_name == None:
            raise Http404()
        
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = f'{self.object.title} - Page - '
        return context

class CreatedByListView(IndexListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._temp_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self._temp_context['user']
        user_full_name = user.username

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
        category_name = self.object_list[0].category.name

        page_title = str(category_name) + ' - ' + ' Categoria - '

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
    

class TagListView(IndexListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._temp_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.object_list[0].tag.first().name

        page_title = str(tag_name) + ' - ' + ' Tag - '

        context.update({
            'page_title': page_title,
        })

        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(tag__slug = self._temp_context['slug'])
        return qs
    
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        tag = models.Tag.objects.filter(slug = slug)

        if slug is None:
            raise Http404()

        self._temp_context.update({
            'slug': slug,
            'tag': tag,
        })

        return super().get(request, *args, **kwargs)




class SearchListView(IndexListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._search_value = ''

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self._search_value = request.GET.get('search', '')
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(Q(title__icontains=self._search_value) | Q(excerpt__icontains=self._search_value) | Q(content__icontains=self._search_value))
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_title = self._search_value[:30] + ' - ' + ' Search - '

        context.update({
            'page_title': page_title,
        })

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self._search_value == '':
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)
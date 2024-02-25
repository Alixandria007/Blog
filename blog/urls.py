from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name= 'index'),
    path('post/<slug:slug>/', views.post, name= 'post'),
    path('page/<slug:slug>', views.page, name= 'page'),
    path('created_by/<int:id>/', views.CreatedByListView.as_view(), name= 'created_by'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name= 'category'),
    path('tag/<slug:slug>/', views.tag, name= 'tag'),
    path('search/', views.search, name= 'search'),
    ]
from django.contrib import admin
from blog import models

# Register your models here.

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    list_per_page = 10
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    list_per_page = 10
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id','title','slug','is_public',
    ordering = '-id',
    list_editable = 'title','is_public',
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'id',
    prepopulated_fields = {
        "slug": ('title',),
    }

@admin.register(models.Post)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id','title','slug','is_public','cover_public','create_at'
    ordering = '-id',
    list_editable = 'title','is_public','cover_public'
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'id',
    prepopulated_fields = {
        "slug": ('title',),
    }


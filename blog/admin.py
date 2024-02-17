from typing import Any
from django_summernote.admin import SummernoteModelAdmin
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
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = 'content',
    list_display = 'id','title','slug','is_public',
    ordering = '-id',
    list_editable = 'is_public',
    list_per_page = 50
    readonly_fields = 'create_at','update_at','created_by', 'update_by'
    list_display_links = 'id',
    prepopulated_fields = {
        "slug": ('title',),
    }

    def save_model(self, request, obj, form, change):

        if change:
            models.Post.update_by = request.user
        else:
            models.Post.created_by = request.user

            
        return super().save_model(request, obj, form, change)


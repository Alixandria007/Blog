from django.contrib import admin
from blog.models import Tag, Category,Page

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id','title','slug','is_public'
    ordering = '-id',
    list_editable = 'title','is_public'
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'id',

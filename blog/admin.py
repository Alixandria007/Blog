from django.contrib import admin
from blog.models import Tag

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    prepopulated_fields = {
        "slug": ('name',),
    }

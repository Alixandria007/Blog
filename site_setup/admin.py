from django.contrib import admin
from django.http import HttpRequest
from site_setup import models

# Register your models here.

@admin.register(models.MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id','text','url_or_file','new_tab'
    ordering = '-id',
    list_editable = 'new_tab',
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'id',

class MenuLinkInline(admin.TabularInline):
    model = models.MenuLink
    extra = 1
    

@admin.register(models.SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description'
    list_display_links = 'id',
    inlines = MenuLinkInline , 

    def has_add_permission(self, request):
        return not models.SiteSetup.objects.exists()
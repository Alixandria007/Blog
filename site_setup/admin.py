from django.contrib import admin
from site_setup import models

# Register your models here.

@admin.register(models.MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id','text','url_or_file','new_tab'
    ordering = '-id',
    list_editable = 'new_tab',
    list_display_links = 'id',
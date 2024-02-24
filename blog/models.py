from typing import Iterable
from utils import images
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Tag(models.Model):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(
        max_length = 255
    )
    slug = models.SlugField(
        unique = True, blank = False, max_length = 255
    )

    def __str__(self) -> str:
        return self.name
    


class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(
        max_length = 255
    )
    slug = models.SlugField(
        unique = True, blank = False, max_length = 255
    )

    def __str__(self) -> str:
        return self.name
    

class Page(models.Model):

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length = 55)
    slug = models.SlugField(
        unique = True, blank = False, max_length = 255
    )

    is_public = models.BooleanField(default = False)

    content = models.TextField()

    def get_absolute_url(self):
        if not self.is_public:
            return reverse('blog:index')
        return reverse('blog:page', args=(self.slug,))


class Post(models.Model):

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(max_length = 55)
    slug = models.SlugField(
        unique = True, blank = False, max_length = 255
    )

    is_public = models.BooleanField(default = False)

    content = models.TextField()
    excerpt = models.CharField(max_length = 255)

    cover = models.ImageField(upload_to='img/%Y/%m', blank=True, null=True, default=None)
    cover_public = models.BooleanField(default = False)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_created_by',
    )
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    update_by = models.ForeignKey(User , on_delete = models.SET_NULL, default = None, blank = True, null = True, related_name = "post_update_by" )

    category = models.ForeignKey("Category", on_delete=models.SET_NULL, default = None, null = True, blank = True)
    tag = models.ManyToManyField(Tag, blank = True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):

        cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False


        
        if self.cover:
            cover_changed = cover_name != self.cover.name

        if cover_changed:
            self.cover = images.resize_images(self.cover, 900, True, 80)

        return super_save
    
    def get_absolute_url(self):
        if not self.is_public:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))
    
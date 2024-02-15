from django.db import models

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
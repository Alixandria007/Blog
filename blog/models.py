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
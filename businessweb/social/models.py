from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Key name", max_length=100, unique=True)
    name = models.CharField(max_length=200, verbose_name="Social network")
    url = models.URLField(verbose_name="Link", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "link"
        verbose_name = "link"
        ordering = ['name']
    
    def __str__(self):
        return self.name
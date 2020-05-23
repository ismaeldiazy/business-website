from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(verbose_name="Content")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    class Meta:
        verbose_name = "page"
        verbose_name = "page"
        ordering = ['title']
    
    def __str__(self):
        return self.title
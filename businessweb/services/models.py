from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitule = models.CharField(max_length=200, verbose_name="Subtitle")
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name="Image", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    class Meta:
        # Invert default order
        ordering = ['-created']

    # String method that returns the model title
    def __str__(self):
        return self.title
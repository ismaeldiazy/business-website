from django.contrib import admin
from .models import Service 

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    # created and updated are read only fields (cannot be modified)
    readonly_fields = ('created', 'updated')

# Register service and configuration
admin.site.register(Service, ServiceAdmin)
from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # To display the values of every post on the blog panel
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    # to config the search engine of the blog panel
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    # config post filter
    list_filter = ('author__username', 'categories__name')

    # creating personalized column (categories is many to many, so it's the only way)
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    # rename the personalized column
    post_categories.short_description = "Categories"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
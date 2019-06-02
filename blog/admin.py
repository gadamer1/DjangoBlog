from django.contrib import admin
from .models import Post
from django_markdownx.markdownx.admin import MarkdownxModelAdmin


class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_date', 'published_date')
    list_filter = ('created_date', 'published_date')
    search_fields = ('title','category')


admin.site.register(Post,BlogPostAdmin)


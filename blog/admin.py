from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin


class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_date', 'mod_date')
    list_filter = ('created_date', 'mod_date')
    search_fields = ('title',)


admin.site.register(Post)


from django.contrib import admin
from .models import Post
from django_markdownx.markdownx.admin import MarkdownxModelAdmin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_date', 'mod_date')
    list_filter = ('created_date', 'mod_date')
    search_fields = ('title',)


admin.site.register(Post)


from django.contrib import admin

from blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Product admin model"""

    list_display = ("id", "title", "created_at",)
    search_fields = ("title",)
    list_filter = ("is_published",)
    readonly_fields = ("views",)

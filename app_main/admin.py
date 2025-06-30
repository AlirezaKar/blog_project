from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Article, Category, Comment, MultiMedia, User

admin.site.register(User)
admin.site.unregister(Group)

admin.sites.AdminSite.site_title = 'مدیریت وبلاگ'
admin.sites.AdminSite.site_header = 'مدیریت وبلاگ'
admin.sites.AdminSite.index_title = 'وبلاگ'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'status', 'user', 'content', 'time_created']
    list_display_links = ['user', 'content']
    ordering = ("-time_created", "time_update")
    list_filter = ("status", "time_created")
    search_fields = ("comment", "content")
    list_editable = ("status",)
    # date_hierarchy = "time_created"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'time_created', 'category']
    list_display_links = ['title', 'user', 'category']
    ordering = ("time_created", "time_update")
    list_filter = ("status", "time_created")
    search_fields = ("title", "description", "content")
    list_editable = ("status", )
    # date_hierarchy = "time_created"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)

@admin.register(MultiMedia)
class MultiMediaAdmin(admin.ModelAdmin):
    list_display = ["article", "time_created"]
    list_display_links = ["article"]
    list_filter = ("time_created",)
    search_fields = ("article",)
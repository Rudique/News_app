from django.contrib import admin
from .models import NewsModel, CommentModel


class CommentModelInline(admin.TabularInline):
    model = CommentModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'active']
    list_filter = ['active']
    inlines = [CommentModelInline]
    actions = ['make_active', 'make_inaktive']

    def make_active(self, request, queryset):
        queryset.update(active=True)

    def make_inaktive(self, request, queryset):
        queryset.update(active=False)

    make_active.short_description = 'Turn into active'
    make_inaktive.short_description = 'Turn into inactive'


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'article']
    list_filter = ['name']
    actions = ['deleted_by_admin']

    def deleted_by_admin(self, request, queryset):
        queryset.update(comment='deleted by administration')

    deleted_by_admin.short_description = 'Delete by admin'


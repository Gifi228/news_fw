from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'views')
    readonly_fields = ('views',)
    list_filter = ('category', 'created_at')




admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)

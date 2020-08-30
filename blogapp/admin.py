from django.contrib import admin
from .models import Post, Category, Comment, Article
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # new

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Post, PostAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)


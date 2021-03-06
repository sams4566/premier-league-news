from django.contrib import admin
from .models import Article, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'approve_category',)
    actions = ['approve_selected_categories']
    search_fields = ['category_name']

    def approve_selected_categories(self, request, list_of_categories):
        list_of_categories.update(approve_category=True)

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('headline', 'approved', 'time_created', 'updated_time', 'author',)
    search_fields = ['headline', 'author',]
    actions = ['approve_selected_articles']
    summernote_fields = ('content')
    
    def approve_selected_articles(self, request, list_of_articles):
        list_of_articles.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'users_name', 'time_created_comment' )
    search_fields = ['article', 'users_name',]
    list_filter = ('article',)

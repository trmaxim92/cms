from django.contrib import admin
from .models import Category, Article



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','author', 'published_at','status')
    list_filter = ('created_at','updated_at','published_at', 'status','author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    
    
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

from django.contrib import admin
from .models import Category, Post
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name',]
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category',]
#     list_filter = ['in_stock', 'is_active']
#     list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

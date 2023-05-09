from django.contrib import admin
from .models import Science
# Register your models here.


@admin.register(Science)
class AdminScience(admin.ModelAdmin):
    list_display=['science_name',]
    prepopulated_fields = {'slug': ('science_name',)}

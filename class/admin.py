from django.contrib import admin
from .models import Group

@admin.register(Group)
class ClassAdmin(admin.ModelAdmin):
    list_display=["group_NumberLetter",'class_curator',]

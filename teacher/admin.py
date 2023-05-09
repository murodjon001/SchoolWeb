from django.contrib import admin
from .models import Teacher,SchoolAdministration,Position
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','science','position','is_active',]


@admin.register(SchoolAdministration)
class SchoolAdministrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','position','science','is_active',]



@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['position','is_active','created'] 
from django.urls import path
from .views import *

app_name = 'school'

urlpatterns = [
    path('', homepage, name='home'),
    # home teacher
    path('teacher_list/', teacherlist, name='teacher_list'),
    path('teacher_details/<int:pk>/', teacher_details, name='teacher_details'),

    #home administration
    path('administration_list', admin_list, name= "admin_list"),
    path('admin_details/<int:pk>/', admin_details, name='admin_details'),

    #conatct
    path('contact/', contact, name="contact"),


]
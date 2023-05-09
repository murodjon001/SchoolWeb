from django.urls import path
from .views import *

app_name = "class"

urlpatterns = [
    path('class_list/', group_list, name="class_list"),
]

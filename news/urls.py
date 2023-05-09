from django.urls import path
from .views import *

app_name= "news"

urlpatterns = [
    path('category_list/<int:pk>/', category_list, name="category_list"),
    path('post_details/<int:pk>/', post_details, name='post_details'),
    
]

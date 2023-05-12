from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def category_list(request, pk):
    category = get_object_or_404(Category, id=pk)

    return render(request, 'news/category_list.html', {"category": category})


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'news/post_details.html', {"post": post})

def all_post(request):
    all_post = Post.objects.all().order_by('-data_created')

    return render(request, 'news/all_post.html', {'all_post': all_post})

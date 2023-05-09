from django.shortcuts import render
from .models import Group
# Create your views here.


def group_list(request):

    group = Group.objects.all().order_by('group_NumberLetter')
    return render(request, 'class/class_list.html', {"class": group})
    
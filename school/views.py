from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from teacher.models import Teacher, SchoolAdministration
from .models import Contact
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def homepage(request):
   

    teachers = Teacher.objects.all().order_by('name')[:4]
    
    return render(request, 'home.html',{"teachers": teachers,})

def teacherlist(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html',{"teachers": teachers,})

def teacher_details(request, pk):
    teachers = get_object_or_404(Teacher, id=pk, is_active=True)
    return render(request, 'teacher/teacher_details.html', {"teacher": teachers})

def admin_list(request):
    admin = SchoolAdministration.objects.all().order_by('name')

    return render(request, "teacher/admin_list.html", {"admin":admin})


def admin_details(request, pk):
    teachers = get_object_or_404(SchoolAdministration, id=pk, is_active=True)
    return render(request, 'teacher/admin_details.html', {"admin": teachers})


def contact(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['text']

        if len(username) < 3:
            return HttpResponse("Ism juda qisqa! >>>")

        else:               
            current_date = timezone.now().date()                               
            new_user = Contact(name=username, phone=phone, description=description, data_create=current_date)
            new_user.save()
            return render(request, 'home.html')
    return render(request, 'contact/contact.html')
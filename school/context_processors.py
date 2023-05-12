from teacher.models import Teacher, SchoolAdministration
from science.models import Science
from news.models import Category,Post

def teachers(request):
    science = Science.objects.all().order_by('science_name')
    director = SchoolAdministration.objects.filter(position__position = "Direktor")
    category = Category.objects.all()
    post = Post.objects.all()
    post_home = Post.objects.all().order_by('-data_created')[:4]

    return{
        # 'teachers': Teacher.objects.all,
        'administrations': SchoolAdministration.objects.all().order_by('name')[:4],
        'director': director,
        'science' : science,
        'categories': category,
        'post': post,
        'post_h': post_home,
    }
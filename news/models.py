from django.db import models
from teacher.models import Teacher

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,blank=False, verbose_name="Bo'lim kategoriyasi")
    slug = models.SlugField(verbose_name=("Category safe URL"), max_length=255, unique=True)
    data_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-data_created",)
        verbose_name =("Kategorya")
        verbose_name_plural =("Kategoriyalar")

    def __str__(self) -> str:
        return self.category_name
    
class Post(models.Model):
    title = models.CharField(max_length=150,blank=True,verbose_name="Mavzu")
    author = models.ForeignKey(Teacher, on_delete=models.RESTRICT, blank=False,verbose_name="Muallif")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, blank=False,verbose_name="Bo'lim kategoriyasi")
    slug = models.SlugField(verbose_name=("Post safe URL"), max_length=255, unique=True)
    photo = models.ImageField(upload_to="images/", verbose_name="Rasm")
    description = models.TextField(blank=False, verbose_name="Tekst")
    data_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-data_created",)
        verbose_name =("Post")
        verbose_name_plural =("Postlar")

    def __str__(self) -> str:
        return self.title